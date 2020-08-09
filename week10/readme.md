TODO: Reflect on what you learned this week and what is still unclear.
#%%
tb_dates['Year'] = tb_dates.index.year
tb_dates['Month'] = tb_dates.index.month
tb_dates.head(3)
# To get the year and month from the dates and put them on separate columns

#%%
date_start_range = tb[tb["started_at"].between('2012-01-01', '2020-12-31')]
known_start = date_start_range['started_at']
date_end_range = tb[tb["read_at"].between('2012-01-01', '2020-12-31')]
known_end = date_end_range['read_at']
# Books from a date range than just dates from set date range
