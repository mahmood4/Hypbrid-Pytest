pytest -v -s  -m "sanity" --capture sys -rP --html=Reports\reports1.html .\testCases\  --browser chrome
pytest -v -s  -m "sanity" --capture sys -rP --html=Reports\reports1.html .\testCases\  --browser firefox

REM pytest -v -s  -m "sanity or regression" --capture sys -rP --html=Reports\reports2.html .\testCases\  --browser chrome
REM pytest -v -s  -m "sanity and regression" --capture sys -rP --html=Reports\reports3.html .\testCases\  --browser chrome
REM pytest -v -s  -m "regression" --capture sys -rP --html=Reports\reports4.html .\testCases\  --browser chrome
