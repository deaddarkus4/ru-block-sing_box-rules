curl -OL https://github.com/deaddarkus4/ru-block-sing_box-rules/releases/latest/download/geoip-ru-block.srs
curl -OL https://github.com/deaddarkus4/ru-block-sing_box-rules/releases/latest/download/geosite-ru-block.srs 
copy geosite-ru-block.srs "%1%\bin\srss"
copy geoip-ru-block.srs "%1%\bin\srss"
del /Q geosite-ru-block.srs
del /Q geoip-ru-block.srs