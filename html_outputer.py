class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html','w')
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
                <th>简介</th>
            </tr>
        ''')

        for data in self.datas:
            print(data)
            str = '''
            <tr>
                <td>%s</td>
                <td>%s</td>
            </tr>
            '''
            fout.write(str % (data['title'] ,data['summary']))


        fout.write(str)

        fout.write("</table></body></html>")