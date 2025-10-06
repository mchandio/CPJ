"""CPJ House Knowledge Features
Provides knowledge-related features like books and libraries for documentation and API references.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Set
from enum import Enum, auto
from cpj_type_system import TypeSystem, TypeKind, WallSection
from cpj_parser2 import Node, NodeType
from cpj_enums import AccessLevel

class KnowledgeKind(Enum):
    """Types of knowledge features"""
    BOOK = auto()        # Single documentation unit (class, function)
    LIBRARY = auto()     # Collection of related documentation
    CATALOG = auto()     # Index of available documentation
    REFERENCE = auto()   # API reference documentation
    MANUAL = auto()      # User manual/guide

@dataclass
class BookPage:
    """Individual page in a book containing documentation"""
    content: str
    page_number: int
    tags: Set[str] = field(default_factory=set)
    references: List[str] = field(default_factory=list)
    examples: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Book(Node):
    """Documentation unit for a single component"""
    title: str = field(default="")
    kind: KnowledgeKind = field(default=KnowledgeKind.BOOK)
    pages: List[BookPage] = field(default_factory=list)
    author: str = field(default="")
    version: str = field(default="1.0.0")
    tags: Set[str] = field(default_factory=set)
    _type_system: Optional[TypeSystem] = field(default=None, init=False)
    
    def __init__(self, type_system: TypeSystem, **kwargs):
        super().__init__(node_type=NodeType.KNOWLEDGE, **kwargs)
        self._type_system = type_system
        self.title = kwargs.get('title', '')
        self.author = kwargs.get('author', '')
        self.version = kwargs.get('version', '1.0.0')
        self.tags = set(kwargs.get('tags', []))
        
    def add_page(self, content: str, tags: Optional[Set[str]] = None,
                references: Optional[List[str]] = None,
                examples: Optional[List[str]] = None) -> BookPage:
        """Add a new page to the book"""
        page = BookPage(
            content=content,
            page_number=len(self.pages) + 1,
            tags=tags or set(),
            references=references or [],
            examples=examples or []
        )
        self.pages.append(page)
        return page
        
    def get_page(self, page_number: int) -> Optional[BookPage]:
        """Get a specific page by number"""
        if 1 <= page_number <= len(self.pages):
            return self.pages[page_number - 1]
        return None
        
    def search(self, query: str) -> List[BookPage]:
        """Search pages for content"""
        query = query.lower()
        return [
            page for page in self.pages
            if query in page.content.lower() or
            any(query in tag.lower() for tag in page.tags)
        ]

@dataclass
class Library(Node):
    """Collection of related documentation"""
    name: str = field(default="")
    kind: KnowledgeKind = field(default=KnowledgeKind.LIBRARY)
    books: Dict[str, Book] = field(default_factory=dict)
    categories: Dict[str, Set[str]] = field(default_factory=dict)
    _type_system: Optional[TypeSystem] = field(default=None, init=False)
    
    def __init__(self, type_system: TypeSystem, **kwargs):
        super().__init__(node_type=NodeType.KNOWLEDGE, **kwargs)
        self._type_system = type_system
        self.name = kwargs.get('name', '')
        
    def add_book(self, book: Book, category: Optional[str] = None) -> bool:
        """Add a book to the library"""
        if book.title in self.books:
            return False
            
        self.books[book.title] = book
        if category:
            self.categories.setdefault(category, set()).add(book.title)
        return True
        
    def get_book(self, title: str) -> Optional[Book]:
        """Get a book by title"""
        return self.books.get(title)
        
    def list_books(self, category: Optional[str] = None) -> List[str]:
        """List all books, optionally filtered by category"""
        if category:
            return sorted(self.categories.get(category, set()))
        return sorted(self.books.keys())
        
    def search(self, query: str) -> Dict[str, List[BookPage]]:
        """Search all books for content"""
        results = {}
        for title, book in self.books.items():
            pages = book.search(query)
            if pages:
                results[title] = pages
        return results

@dataclass
class Catalog(Node):
    """Index and search system for documentation"""
    name: str = field(default="")
    kind: KnowledgeKind = field(default=KnowledgeKind.CATALOG)
    libraries: Dict[str, Library] = field(default_factory=dict)
    index: Dict[str, Set[str]] = field(default_factory=dict)  # term -> book titles
    _type_system: Optional[TypeSystem] = field(default=None, init=False)
    
    def __init__(self, type_system: TypeSystem, **kwargs):
        super().__init__(node_type=NodeType.KNOWLEDGE, **kwargs)
        self._type_system = type_system
        self.name = kwargs.get('name', '')
        
    def add_library(self, library: Library):
        """Add a library to the catalog"""
        self.libraries[library.name] = library
        self._update_index(library)
        
    def search(self, query: str) -> Dict[str, Dict[str, List[BookPage]]]:
        """Search across all libraries"""
        results = {}
        for lib_name, library in self.libraries.items():
            lib_results = library.search(query)
            if lib_results:
                results[lib_name] = lib_results
        return results
        
    def _update_index(self, library: Library):
        """Update search index with library contents"""
        for book in library.books.values():
            for page in book.pages:
                # Index content words
                words = set(word.lower() for word in page.content.split())
                for word in words:
                    self.index.setdefault(word, set()).add(book.title)
                # Index tags
                for tag in page.tags:
                    self.index.setdefault(tag.lower(), set()).add(book.title)

@dataclass
class Reference(Node):
    """API reference documentation"""
    name: str = field(default="")
    kind: KnowledgeKind = field(default=KnowledgeKind.REFERENCE)
    signatures: Dict[str, str] = field(default_factory=dict)
    descriptions: Dict[str, str] = field(default_factory=dict)
    examples: Dict[str, List[str]] = field(default_factory=dict)
    see_also: Dict[str, List[str]] = field(default_factory=dict)
    _type_system: Optional[TypeSystem] = field(default=None, init=False)
    
    def __init__(self, type_system: TypeSystem, **kwargs):
        super().__init__(node_type=NodeType.KNOWLEDGE, **kwargs)
        self._type_system = type_system
        self.name = kwargs.get('name', '')
        
    def add_entry(self, name: str, signature: str, description: str,
                examples: Optional[List[str]] = None,
                see_also: Optional[List[str]] = None):
        """Add an API reference entry"""
        self.signatures[name] = signature
        self.descriptions[name] = description
        if examples:
            self.examples[name] = examples
        if see_also:
            self.see_also[name] = see_also
            
    def get_entry(self, name: str) -> Optional[Dict[str, Any]]:
        """Get an API reference entry"""
        if name not in self.signatures:
            return None
            
        return {
            'name': name,
            'signature': self.signatures[name],
            'description': self.descriptions[name],
            'examples': self.examples.get(name, []),
            'see_also': self.see_also.get(name, [])
        }
        
    def search(self, query: str) -> List[str]:
        """Search API reference entries"""
        query = query.lower()
        return [
            name for name in self.signatures.keys()
            if query in name.lower() or
            query in self.descriptions[name].lower()
        ]