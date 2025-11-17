@echo off
call npm run build  -- --minify false

set source_folder=dist
set destination_folder=..\view

xcopy /s /y "%source_folder%" "%destination_folder%"
echo 文件已复制完成。