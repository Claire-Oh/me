TODO: Reflect on what you learned this week and what is still unclear.

#%%
read_shelf = r.get(
    f"{base}/review/list/{usernum}.xml?" 
    f"key={key}&v=2" "&shelf=read" "&per_page=200"
)
xml_data = read_shelf.content
read_books = xmltodict.parse(xml_data)
rb = read_books["GoodreadsResponse"]["reviews"]["review"]
books = pd.DataFrame(rb) ## pd --> pandas

Notes:
Lines 10: pandas.DataFrame is two-dimensional size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns).
A Data frame is a two-dimensional data structure in a tabular fashion in rows and columns.
Basically creates a table using "rb"


#%%
books.sample(4)


#%%
books.columns


#%%
books.drop(
    [
        "votes",
        "spoiler_flag",
        "spoilers_state",
        "shelves",
        "recommended_for",
        "recommended_by",
        "read_count",
        "body",
        "comments_count",
        "link",
        "owned",
    ],
    axis=1,
    inplace=True,
)

Notes:
Lines 27-43: Dropping columns from books

#%%
dead_date = parser.parse("2017 12 01 00:00:00 -0800")

Notes
Line 49: parser offers a generic date/time string parser which
is able to parse most known formats to represent a date and/or time. 