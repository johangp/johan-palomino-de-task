from dataclasses import asdict, dataclass


@dataclass
class RawResults:
    results_id: str
    status: str
    copyright: str
    num_results: int
    bestsellers_date: str
    published_date: str
    created_at: str

    def dict(self):
        return asdict(self)


@dataclass
class RawList:
    list_id: int
    results_id: str
    list_name: str
    display_name: str
    updated: str
    list_image: str
    created_at: str

    def dict(self):
        return asdict(self)


@dataclass
class RawBook:
    list_id: int
    results_id: str
    age_group: str
    author: str
    contributor: str
    contributor_note: str
    description: str
    price: float
    primary_isbn13: str
    primary_isbn10: str
    publisher: str
    rank: int
    title: str
    created_date: str
    updated_date: str
    created_at: str

    def dict(self):
        return asdict(self)
