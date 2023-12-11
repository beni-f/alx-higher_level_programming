#!/usr/bin/node
let x = Math.floor(Number(process.argv[2]));
if (isNaN(x) || x <= 0)
    console.log('Missing Size');
else
{
    for (let i = 0; i < x; i++)
    {
        let val = '';
        for (let j = 0; j < x; j++)
        {
            val += 'X'
        }
        console.log(val);
    }
}