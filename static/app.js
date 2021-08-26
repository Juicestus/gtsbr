/**
 * @file app.js
 * 
 * Host a series of Markdown files on GitHub
 * as a static web application.
 * 
 * @author Justus Languell, 2021
 * @copyright Texas Torque, 2021
 */

const HOST = 'https://raw.githubusercontent.com/TexasTorque/Wiki/main';

var indexReq = new XMLHttpRequest();
indexReq.open('GET', HOST + '/index.json', false);
indexReq.send(null);
var index = JSON.parse(indexReq.responseText);

var header = "<p>";
for (var [key, value] of Object.entries(index)) {
    header += `<a href="${value}">${key}</a> &#8226; `;
}
header = header.substr(0, header.length - 8) + "</p>";


var convertor = new showdown.Converter();
var path = window.location.pathname.split('.')[0];

if (path == '/') {
    window.location.href = '/readme';
}

var pageReq = new XMLHttpRequest();
pageReq.open('GET', HOST + path + '.md', false);
pageReq.send(null);
var content = pageReq.responseText;

content = content.replaceAll('[ ]', '☐')
content = content.replaceAll('[x]', '☒')
content = convertor.makeHtml(content);
content = content.replace(/<img src=\"(.*?)\"/g, "<br><img src=\"" + HOST + '/$1"');
document.getElementById('content').innerHTML = header + content;
