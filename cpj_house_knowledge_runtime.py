"""Runtime management for knowledge features."""

from typing import Dict, Any, Optional, List, Set
from cpj_type_system import TypeSystem
from cpj_house_knowledge import (
    Book, Library, Catalog, Reference,
    KnowledgeKind, BookPage
)

class KnowledgeManager:
    """Manages knowledge features in the house"""
    
    def __init__(self, type_system: TypeSystem):
        self._type_system = type_system
        self._books = {}
        self._libraries = {}
        self._catalogs = {}
        self._references = {}
        
    def create_book(self, title: str, author: str = "", version: str = "1.0.0",
                   tags: Optional[Set[str]] = None) -> Book:
        """Create a new book for documentation"""
        book = Book(
            type_system=self._type_system,
            title=title,
            author=author,
            version=version,
            tags=tags or set()
        )
        self._books[title] = book
        return book
        
    def create_library(self, name: str) -> Library:
        """Create a new library for document collection"""
        library = Library(
            type_system=self._type_system,
            name=name
        )
        self._libraries[name] = library
        return library
        
    def create_catalog(self, name: str) -> Catalog:
        """Create a new catalog for documentation indexing"""
        catalog = Catalog(
            type_system=self._type_system,
            name=name
        )
        self._catalogs[name] = catalog
        return catalog
        
    def create_reference(self, name: str) -> Reference:
        """Create a new API reference"""
        reference = Reference(
            type_system=self._type_system,
            name=name
        )
        self._references[name] = reference
        return reference
        
    def get_book(self, title: str) -> Optional[Book]:
        """Get a book by title"""
        return self._books.get(title)
        
    def get_library(self, name: str) -> Optional[Library]:
        """Get a library by name"""
        return self._libraries.get(name)
        
    def get_catalog(self, name: str) -> Optional[Catalog]:
        """Get a catalog by name"""
        return self._catalogs.get(name)
        
    def get_reference(self, name: str) -> Optional[Reference]:
        """Get an API reference by name"""
        return self._references.get(name)
        
    def list_books(self) -> List[str]:
        """List all book titles"""
        return sorted(self._books.keys())
        
    def list_libraries(self) -> List[str]:
        """List all library names"""
        return sorted(self._libraries.keys())
        
    def list_catalogs(self) -> List[str]:
        """List all catalog names"""
        return sorted(self._catalogs.keys())
        
    def list_references(self) -> List[str]:
        """List all API reference names"""
        return sorted(self._references.keys())
        
    def search_all(self, query: str) -> Dict[str, Any]:
        """Search across all knowledge features"""
        results = {
            'books': {},
            'libraries': {},
            'references': []
        }
        
        # Search individual books
        for title, book in self._books.items():
            pages = book.search(query)
            if pages:
                results['books'][title] = pages
                
        # Search libraries
        for name, library in self._libraries.items():
            lib_results = library.search(query)
            if lib_results:
                results['libraries'][name] = lib_results
                
        # Search API references
        for name, reference in self._references.items():
            ref_results = reference.search(query)
            if ref_results:
                results['references'].extend(ref_results)
                
        return results
        
    def generate_documentation(self, format: str = "markdown") -> str:
        """Generate complete documentation"""
        if format == "markdown":
            return self._generate_markdown_docs()
        # Could add other format support (HTML, RST, etc.)
        return ""
        
    def _generate_markdown_docs(self) -> str:
        """Generate documentation in Markdown format"""
        docs = ["# CPJ Documentation\n\n"]
        
        # Add API References
        docs.append("## API Reference\n\n")
        for name, reference in sorted(self._references.items()):
            docs.append(f"### {name}\n\n")
            for entry_name in sorted(reference.signatures.keys()):
                entry = reference.get_entry(entry_name)
                if entry:
                    docs.append(f"#### {entry_name}\n\n")
                    docs.append(f"```python\n{entry['signature']}\n```\n\n")
                    docs.append(f"{entry['description']}\n\n")
                    if entry['examples']:
                        docs.append("Examples:\n")
                        for example in entry['examples']:
                            docs.append(f"```python\n{example}\n```\n\n")
                    if entry['see_also']:
                        docs.append("See also: " + ", ".join(entry['see_also']) + "\n\n")
                        
        # Add Books
        docs.append("## Documentation\n\n")
        for title, book in sorted(self._books.items()):
            docs.append(f"### {title}\n\n")
            docs.append(f"Version: {book.version}\n\n")
            if book.author:
                docs.append(f"Author: {book.author}\n\n")
            for page in book.pages:
                docs.append(f"#### Page {page.page_number}\n\n")
                docs.append(f"{page.content}\n\n")
                if page.examples:
                    docs.append("Examples:\n")
                    for example in page.examples:
                        docs.append(f"```python\n{example}\n```\n\n")
                        
        return "".join(docs)