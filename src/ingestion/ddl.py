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
