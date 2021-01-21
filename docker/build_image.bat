
@ECHO OFF

docker build --no-cache -t "pintutorial" ^
    --build-arg myuser="%USERNAME%" ^
    --build-arg myuid=11011 ^
    --build-arg mygroup="%USERNAME%" ^
    --build-arg mygid=11011 ^
      -f ./image.dockerfile .

