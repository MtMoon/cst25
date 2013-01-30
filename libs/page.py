from django.db.models.query import QuerySet

def get_page_dict(query, npp, urlp, curr):
    """ Get a page dict.
    Arguments:
    query -> The QuerySet object
    npp   -> The number of records shown per page.
    urlp  -> The formatted string of url to show each page.
             e.g. "/photo/album/2/{0}/"
    curr  -> Current page number.
    Returns:
    { current: curr, total: <Total number of pages>,
      prev: <URL of previous page>,
      next: <URL of next page> }
    If no previous or next page, the corresponding URL is ''
    """
    nrec = query.count()
    totnum = (nrec + npp - 1) / npp
    if totnum == 0:
        totnum = 1
    page = {'current': curr,
            'total': totnum}
    page['prev'] = urlp.format(curr-1)
    page['next'] = urlp.format(curr+1)
    if curr == 1:
        page['prev'] = ''
    if curr == totnum:
        page['next'] = ''
    return page

def apage(query, nr, npp):
    """ Get a page of records in a query.
    Arguments:
    nr -> Page number.
    npp -> The number of elements shown in a page.
    """
    return query[(nr-1)*npp : nr*npp]
