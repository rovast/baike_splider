# -*- coding: utf-8 -*-
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w',encoding='utf-8')
        fout.write('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>采集结果</title>
        </head>
        <body>
        <table>
            <tr>
                <th width="100">词条名</th>
                <th>url</th>
                <th>简介</th>
            </tr>
        ''')

        for data in self.datas:
            fout.write("<str>")
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")
        fout.write('''
                </table>
            </body>
            <style type="text/css">
                table{border-collapse: collapse;padding: 50px;}
                th{text-align: center;vertical-align: center}
                td{text-align: left;}
                th,td{border: 1px solid #ccc;font-size:12px;line-height:20px;padding:10px;}
            </style>
        </html>''')
