from jinja2 import Environment, FileSystemLoader, meta
import sys


def main():
    print(sys.argv[1])
    env = Environment(loader=FileSystemLoader(('nginx-templates/', 'mysql-templates/')))
    template_source = env.loader.get_source(env, sys.argv[1])[0]
    template = env.get_template(sys.argv[1])
    parsed_content = env.parse(template_source)
    tags = meta.find_undeclared_variables(parsed_content)
    tags_input = {}
    for tag in tags:
        print 'Please enter value for ' + tag
        temp = raw_input()
        if temp.count(',') :
            value_list = temp.split(',')
            tags_input[tag] = value_list
        else :
            tags_input[tag] = [temp]
    print(template.render(tags_input))

if __name__ == "__main__":
    main()
