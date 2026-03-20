-- 코드를 작성해주세요
select count(*) as FISH_COUNT
from fish_info fi 
    join fish_name_info fni on fi.fish_type = fni.fish_type
where fni.fish_name in ('BASS', 'SNAPPER');