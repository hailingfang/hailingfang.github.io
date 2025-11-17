import jinja2
import os


def render(jinja_env, temp_file, dst_dire=None, data_dic=None):
    template = jinja_env.get_template(temp_file)
    template_rendered = template.render(data_dic=data_dic)
    if dst_dire:
        if not os.path.exists(dst_dire):
            os.mkdir(dst_dire)
        outfile = os.path.join(dst_dire, "index.html")
    else:
        outfile = "index.html"
    fout = open(outfile, "w")
    fout.write(template_rendered)
    fout.close()


def main():
    env = jinja2.Environment(loader=jinja2.FileSystemLoader("templates"))

    #render index.html
    render(env, "index.html")

    #render about-me/index.html
    render(env, "about-me.html", "about-me")

    #render life/index.html
    render(env, "life.html", "life")

    #render study/index.html
    render(env, "study.html", "study")

    #render documentation/index.html
    render(env, "documentation.html", "documentation")



if __name__ == "__main__":
    main()
