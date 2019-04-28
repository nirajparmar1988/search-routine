## Raik = not available


## Cache create for result 1
curl -s -X PUT -H "Content-Type: text/plain" -d "0,1,2,3,4,5,6" "http://$RIAK_HTTP_IP:$RIAK_HTTP_PORT/buckets/$RIAK_TEST_BUCKET/keys/"OR-Care,Quality,Commission"

## Cache create for result 2
Cache create for result 2
curl -s -X PUT -H "Content-Type: text/plain" -d "9" "http://$RIAK_HTTP_IP:$RIAK_HTTP_PORT/buckets/$RIAK_TEST_BUCKET/keys/"OR-September,2004"

## Cache create for result 3
Cache create for result 3
curl -s -X PUT -H "Content-Type: text/plain" -d "6,8" "http://$RIAK_HTTP_IP:$RIAK_HTTP_PORT/buckets/$RIAK_TEST_BUCKET/keys/"OR-general,population,generally"

## Cache create for result 4
Cache create for result 4
curl -s -X PUT -H "Content-Type: text/plain" -d "1" "http://$RIAK_HTTP_IP:$RIAK_HTTP_PORT/buckets/$RIAK_TEST_BUCKET/keys/"AND-Care,Quality,Commission,admission"

## Cache create for result 5
Cache create for result 5
curl -s -X PUT -H "Content-Type: text/plain" -d "6" "http://$RIAK_HTTP_IP:$RIAK_HTTP_PORT/buckets/$RIAK_TEST_BUCKET/keys/"AND-general,population,Alzheimer"


$KEY = "OR-Care,Quality,Commission"

## Retrive data from cache 
Retrive data from cache 
CACHE_VALUE=$(redis-cli -h "$CACHE_PROXY_IP" -p "$CACHE_PROXY_PORT" "$RIAK_TEST_BUCKET:$KEY")



## Insert value with index for document-1 
curl -v -XPUT http://localhost:8098/types/indexes/buckets/hscicNews/keys/1 \
  -H "x-riak-index-month_bin: June" \
  -H "x-riak-index-year_int: 2013" \
  -H "Content-Type: text/plain" \
  -d "June 5 , 2013 : The majority of ..." 
 
## Insert value with index for document-2 
curl -v -XPUT http://localhost:8098/types/indexes/buckets/hscicNews/keys/1 \
  -H "x-riak-index-month_bin: July" \
  -H "x-riak-index-year_int: 2013" \
  -H "Content-Type: text/plain" \
  -d "July 9 , 2013 : The HSCIC has extended ..." 

## Insert value with index for document-2 
curl -v -XPUT http://localhost:8098/types/indexes/buckets/hscicNews/keys/1 \
  -H "x-riak-index-month_bin: July" \
  -H "x-riak-index-year_int: 2013" \
  -H "Content-Type: text/plain" \
  -d "July 9 , 2013 : The HSCIC has extended ..." 
 
## Insert value with index for document-3 
curl -v -XPUT http://localhost:8098/types/indexes/buckets/hscicNews/keys/1 \
  -H "x-riak-index-month_bin: June" \
  -H "x-riak-index-year_int: 2013" \
  -H "Content-Type: text/plain" \
  -d "June 19 , 2013 : New figures from the Health ..." 

## Insert value with index for document-4 
curl -v -XPUT http://localhost:8098/types/indexes/buckets/hscicNews/keys/1 \
  -H "x-riak-index-month_bin: June" \
  -H "x-riak-index-year_int: 2013" \
  -H "Content-Type: text/plain" \
  -d "June 13 , 2013 : Almost one in five women ..." 

## Display key for document June 2013(using secondary index)
curl http://localhost:8098/buckets/hscicNews/index/month_bin/June

