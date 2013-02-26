from jinja2 import Environment, FileSystemLoader, meta
import sys, string, random, requests, gzip

values_used = {}
def main():
    """Opens the recipe file specified on the command line, the calls the defined handlers for each instruction"""
    recipe_file = open('recipes/'+sys.argv[1])
    recipe = recipe_file.readlines()
    recipe = [line.rstrip().split(' ')for line in recipe]
    for line in recipe :
        globals()[line[0]](line)

def mine_salt(char):
    """Generates random strings of char length for salts and keys, loaded as a Jinja filter in the fill_template method"""
    chars = string.uppercase + string.lowercase + string.digits + '%&!@#$ '
    salt = [random.choice(chars) for x in range(char)]
    return ''.join(salt)

def tar_get(url):
    r = requests.get(url)
    tar_file = open(stringIO(r.content))

def fill_template(param_list):
    env = Environment(loader=FileSystemLoader(('nginx-templates/', 'mysql-templates/', 'temp/', 'misc-templates/')))
    env.filters['mine_salt'] = mine_salt
    try:
        template_source = env.loader.get_source(env, param_list[1])[0]
    except:
        raise NameError('Template Name invalid, please check recipe')
    template = env.get_template(template_name)
    parsed_content = env.parse(template_source)
    tags = meta.find_undeclared_variables(parsed_content)
    tags_input = {}
    for tag in tags:
        if tag in values_used:
            tags_input[tag] = values_used[tag]
        else :
            print 'Please enter value for ' + tag
            temp = raw_input()
            if temp.count(' ') :
                value_list = temp.split(' ')
                tags_input[tag] = value_list
                values_used[tag] = value_list
            else :
                tags_input[tag] = [temp]
                values_used[tag] = [temp]
    print(template.render(tags_input))

if __name__ == "__main__":
    main()
