raw_results_ddl = """
create table if not exists raw_results (
    results_id varchar not null, 
    status varchar not null,          
    copyright text not null,              
    num_results integer not null,         
    bestsellers_date date not null,       
    published_date date not null,         
    created_at date not null
);"""

raw_lists_ddl = """
create table if not exists raw_lists (
	list_id integer not null,
	results_id varchar not null,
	list_name varchar not null,
	display_name varchar not null,
	updated varchar not null,
	list_image varchar not null,
	created_at date not null
);
"""
