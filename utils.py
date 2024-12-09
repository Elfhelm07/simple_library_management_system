def paginate(items, page: int, per_page: int):
    start = (page - 1) * per_page
    end = start + per_page
    return items[start:end]