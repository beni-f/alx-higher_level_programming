#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function(err, resp, body){
    if(err)
    {
        console.error(err);
        return;
    }
    let response = JSON.parse(body);
    let obj = {}
    for (const result of response) {
        if(result["completed"] == true)
        {
            if(obj[result["userId"]] !== undefined)
                obj[result["userId"]]++;
            else{
                obj[result["userId"]] = 1;
            }
        }
    }
    console.log(obj);
})