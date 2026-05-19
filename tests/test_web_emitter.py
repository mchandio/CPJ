import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.cpj_parser import Parser, WebBlock
from tools.cpj_web_emitter import WebEmitter, emit_file, emit_project


def test_parser_preserves_nested_web_block():
    ast = Parser(
        '''
web {
    title "Nested"
    section features {
        grid {
            card "A" "B"
        }
    }
}
'''
    ).parse()

    block = next(item for item in ast.items if isinstance(item, WebBlock))

    assert 'section features {' in block.lines
    assert 'grid {' in block.lines
    assert block.lines.count('}') == 2


def test_web_emitter_generates_standalone_html():
    ast = Parser(
        '''
web {
    title "CPJ Web Engineering"
    meta description "Standalone web output."
    pwa "CPJ Web Engineering"
    server port 9090
    middleware security {
        header "X-Content-Type-Options" "nosniff"
        cors "*"
        request-id true
    }
    pipeline production {
        use security
        header "X-CPJ-Pipeline" "production"
        require-header "X-CPJ-Token" "dev-token" path "/api/protected"
    }
    service site_config {
        value tier "standalone"
        env mode "CPJ_MODE" "development"
    }
    guard upload_token {
        path "/api/uploads/media"
        token "dev-token"
    }
    template shell {
        section shell {
            h2 "Template shell"
            slot content
        }
    }
    bundle app {
        target es2022
        module esm
        types true
        export CPJ
    }
    marketplace CPJHub {
        registry "local"
        plugin seo "SEO Helper" "1.0.0" "Metadata hooks"
        hook seo head "<meta name='robots' content='index'>"
    }
    container cards {
        selector ".cpj-card"
        min-width "360px"
        css ".cpj-card { border-color: var(--cpj-primary); }"
    }
    animation fade {
        duration "200ms"
        from "opacity: 0;"
        to "opacity: 1;"
        apply ".cpj-card"
    }
    component stack_badge {
        badge "Full stack"
    }
    api "/api/health" {
        json status "ok"
        json cpj true
    }
    api "/api/contact" {
        method POST
        inject site_config
        json status "received"
    }
    api "/api/protected" {
        json status "secret"
    }
    store Lead {
        field name text required
        field email text required
        seed name "Ada" email "ada@example.com"
    }
    migration lead_v2 {
        store Lead
        add-field source text
        index email unique
    }
    upload media {
        path "/api/uploads/media"
        dir "uploads/media"
        accept "text/plain"
        max-bytes 2048
    }
    model Contact {
        field email email required
    }
        cms CPJPress {
            blog "/blog"
            admin "/admin"
            storage "cpjpress_content.json"
            user admin admin admin "Administrator"
            comment "hello" "Reader" "Nice."
            media hero "Hero" "/hero.png" "Hero"
            plugin seo "SEO Helper" "Metadata hooks"
            post "hello" "Hello" "World"
        }
    nav "Home" "#hero"
    hero {
        use stack_badge
        h1 "Build browser apps in CPJ"
        button "Explore" -> "#features"
    }
    route "/dashboard" extends shell {
        h1 "Dashboard"
    }
    section features {
        grid {
            card "Single-file output" "No external runtime is required."
        }
    }
    section contact {
        form signup -> "/api/contact" POST {
            input email "Email" email required
            button "Send"
        }
    }
}
'''
    ).parse()

    html = WebEmitter().emit(ast)

    assert "<!doctype html>" in html
    assert "<title>CPJ Web Engineering</title>" in html
    assert 'href="#features"' in html
    assert 'data-cpj-form="signup"' in html
    assert 'data-cpj-endpoint="/api/contact"' in html
    assert 'required="required"' in html
    assert 'rel="manifest"' in html
    assert 'type="submit" data-cpj-action="send"' in html
    assert "const CPJ = window.CPJ" in html
    assert "serviceWorker" in html
    assert "robots" in html
    assert "@container cards" in html
    assert "@keyframes fade" in html
    assert "No external runtime is required." in html

    server = WebEmitter()
    project_html = server.emit(ast)
    assert "/api/health" in server.server_source(project_html)
    assert "Template shell" in server.server_source(project_html)
    assert server.openapi_spec()["paths"]["/api/health"]["get"]
    assert server.openapi_spec()["paths"]["/api/contact"]["post"]
    assert server.openapi_spec()["paths"]["/__cpj/services"]["get"]
    assert server.openapi_spec()["paths"]["/__cpj/plugins"]["get"]
    assert server.openapi_spec()["paths"]["/api/store/lead"]["get"]
    assert server.openapi_spec()["paths"]["/api/uploads/media"]["post"]
    assert server.openapi_spec()["paths"]["/api/posts"]["get"]
    assert server.openapi_spec()["paths"]["/api/comments"]["post"]
    assert "from cpjpress_runtime import run_site" in server.server_source(project_html)
    assert server.design_tokens()["models"]["contact"][0]["required"] is True
    assert server.design_tokens()["cms"]["name"] == "CPJPress"
    assert server.design_tokens()["pwa"]["name"] == "CPJ Web Engineering"
    assert server.design_tokens()["stores"]["lead"]["fields"][0]["name"] == "name"
    assert server.design_tokens()["services"]["site_config"]["values"]["tier"] == "standalone"
    assert server.design_tokens()["migrations"][0]["add_fields"][0]["name"] == "source"
    assert server.design_tokens()["bundle"]["name"] == "app"
    assert server.component_inventory()["guards"][0]["path"] == "/api/uploads/media"
    assert server.component_inventory()["pipelines"][0]["name"] == "production"
    assert server.component_inventory()["templates"] == ["shell"]
    assert server.diagnostics()["summary"]["warnings"] == 0


def test_emit_file_writes_html(tmp_path):
    source = tmp_path / "app.cpj"
    output = tmp_path / "app.html"
    source.write_text(
        '''
web {
    title "File Emit"
    hero {
        h1 "Ready"
    }
}
''',
        encoding="utf-8",
    )

    written = emit_file(source, output)

    assert written == output
    assert output.exists()
    assert "<h1>Ready</h1>" in output.read_text(encoding="utf-8")


def test_emit_project_writes_full_stack_artifacts(tmp_path):
    source = tmp_path / "app.cpj"
    project = tmp_path / "site"
    source.write_text(
        '''
web {
    title "Project Emit"
    pwa "Project Emit"
    middleware security {
        header "X-Content-Type-Options" "nosniff"
        request-id true
    }
    pipeline production {
        use security
        header "X-CPJ-Pipeline" "production"
    }
    service config {
        value mode "test"
    }
    api "/api/health" {
        json status "ok"
    }
    api "/api/contact" {
        method POST
        json status "received"
    }
    store Lead {
        field name text required
        seed name "Ada"
    }
    migration lead_v2 {
        store Lead
        add-field source text
        index name
    }
    bundle app {
        target es2022
        types true
    }
    marketplace CPJHub {
        registry "local"
        plugin seo "SEO Helper" "1.0.0" "Metadata hooks"
    }
    upload media {
        path "/api/uploads/media"
        dir "uploads/media"
        accept "text/plain"
    }
    cms CPJPress {
        user admin admin admin "Administrator"
        comment "hello" "Reader" "Nice."
        media hero "Hero" "/hero.png" "Hero"
        plugin seo "SEO Helper" "Metadata hooks"
        post "hello" "Hello" "World"
    }
    route "/dashboard" {
        h1 "Dashboard"
    }
    hero {
        h1 "Ready"
    }
}
''',
        encoding="utf-8",
    )

    written = emit_project(source, project)

    assert written == project
    assert (project / "index.html").exists()
    assert (project / "server.py").exists()
    assert (project / "cpjpress_runtime.py").exists()
    assert (project / "manifest.webmanifest").exists()
    assert (project / "sw.js").exists()
    assert (project / "openapi.json").exists()
    assert (project / "design.tokens.json").exists()
    assert (project / "plugins.marketplace.json").exists()
    assert (project / "app.bundle.js").exists()
    assert (project / "app.d.ts").exists()
    assert (project / "tsconfig.json").exists()
    assert (project / "diagnostics.json").exists()
    assert (project / "cpjpress_content.json").exists()
    assert "/api/health" in (project / "server.py").read_text(encoding="utf-8")
    assert "ASSETS" in (project / "server.py").read_text(encoding="utf-8")
    assert "STORES" in (project / "server.py").read_text(encoding="utf-8")
    assert "UPLOADS" in (project / "server.py").read_text(encoding="utf-8")
    assert "MIGRATIONS" in (project / "server.py").read_text(encoding="utf-8")
    assert "PIPELINES" in (project / "server.py").read_text(encoding="utf-8")
    assert "SERVICES" in (project / "server.py").read_text(encoding="utf-8")
    assert "/api/posts" in (project / "openapi.json").read_text(encoding="utf-8")
    assert "/api/contact" in (project / "openapi.json").read_text(encoding="utf-8")
    assert "/api/store/lead" in (project / "openapi.json").read_text(encoding="utf-8")
    content = json.loads((project / "cpjpress_content.json").read_text(encoding="utf-8"))
    assert content["users"][0]["username"] == "admin"
    assert "password_hash" in content["users"][0]
    assert content["comments"][0]["post"] == "hello"
    assert content["media"][0]["slug"] == "hero"
    assert content["plugins"][0]["slug"] == "seo"
