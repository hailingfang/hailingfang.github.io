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


def read_tsv_data(file_name):
    fin = open(file_name)
    data_out = [line.rstrip().split('\t') for line in fin][1:]
    fin.close()
    for line in data_out:
        for idx,ele in enumerate(line):
            if ele == "NA":
                line[idx] = ""
    return data_out



def main():
    env = jinja2.Environment(loader=jinja2.FileSystemLoader("templates"))

    #render index.html
    render(env, "index.html")

    #render about-me/index.html
    edu_data_file = "templates/data/about-me-education.tsv"
    exp_data_file = "templates/data/about-me-experience.tsv"
    pub_data_file = "templates/data/about-me-publication.tsv"
    timeline_data_file = "templates/data/about-me-timeline.tsv"
    about_me_data = {}
    about_me_data["edu"] = read_tsv_data(edu_data_file)
    about_me_data["exp"] = read_tsv_data(exp_data_file)
    about_me_data["pub"] = read_tsv_data(pub_data_file)
    about_me_data["timeline"] = read_tsv_data(timeline_data_file)
    render(env, "about-me.html", "about-me", about_me_data)

    #render life/index.html
    render(env, "life.html", "life")

    #render study/index.html
    render(env, "study.html", "study")

    #render documentation/index.html
    render(env, "documentation.html", "documentation")



if __name__ == "__main__":
    main()
