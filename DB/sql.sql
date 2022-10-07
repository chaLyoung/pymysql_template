/*0 select has_same_resort_name */
select resort_code
from ski_resort
where resort_name = '{resort_name}';

/*1 select last_resort_code */
select resort_code
    , resort_name
    , resort_address
from ski_resort
order by resort_code
desc LIMIT 1;

/*2 insert resort */
insert into ski_resort
values (
    '{resort_code}'
    , '{resort_name}'
    , '{resort_address}'
    , '{resort_phone_no}'
    , '{start_time}'
    , '{end_time}'
    , default
    , default
    , now()
);

/*3 select last_slope_code */
select slope_code
from ski_slope
order by slope_code
desc LIMIT 1;

/*4 insert slope */
insert into ski_slope
values (
    '{resort_code}'
    , '{slope_code}'
    , '{slope_name}'
    , '{slope_level}'
    , default
    , now()
);

/*3 select last_slope_time_code */
select slope_time_code
from slope_time
order by slope_time_code
desc LIMIT 1;

/*4 insert slope_time */
insert into slope_time
    (
        resort_code
        , slope_code
        , slope_time_code
        , slope_time_name
        , start_time
        , end_time
    )
values (%s, %s, %s, %s, %s, %s);

-- concat(@rownum := @rownum + 1) as rownum,