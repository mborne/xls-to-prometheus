import sys
import json
import pyexcel as pe

from jinja2 import Environment, FileSystemLoader, select_autoescape

def main(argv):
    path = argv[0]
    records = pe.iget_records(file_name=path)
    pe.free_resources()
    # for record in records:
    #     print("%s %s" % (record['name'], record['url']))

    jinjaEnv = Environment(
        loader=FileSystemLoader(searchpath="templates/"),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = jinjaEnv.get_template('prometheus.yml.j2')
    for record in records:
        content = template.render(record=record)
        print(content)

if __name__ == "__main__":
    main(sys.argv[1:])
