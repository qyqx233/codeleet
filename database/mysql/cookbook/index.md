```sql
create table employees (
    emp_no int not null,
    birth_date date not null,
    first_name varchar(14) not null,
    last_name varchar(16) not null,
    gender enum('M', 'F') not null,
    hire_date date not null,
    primary key (emp_no),
    key name (first_name, last_name),
    key last_name (last_name)
)
```


索引操作集合
```sql
-- 列出表的索引
show index from employees;

-- 新增一个如果代码里面需要使用函数，此时索引无法生效，可以建立一个虚列，指向该值
alter table employees add hire_date_year year as (year(hire_date)) virtual, add index (hire_date_year);

-- 将索引置为不可用
alter table employees alter index last_name invisible;

-- 降序索引，order by的时候有升降序，这需要建立降序索引
alter table employees add index name_desc (first_name asc, last_name desc);
```

