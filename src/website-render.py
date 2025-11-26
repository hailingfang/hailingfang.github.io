import jinja2
import os
import shutil
import datetime


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
    data_out.reverse()
    return data_out


def format_mark_data(date_str):
    year = int(date_str[: 4])
    month = int(date_str[4: 6])
    day = int(date_str[6: 8])
    hour = date_str[8: 10]
    minute = date_str[10: 12]

    date_time = datetime.datetime(year, month, day)

    date_time_str = date_time.strftime("%b %d, %Y")
    if hour and minute:
        date_time_str = hour + ":" + minute + " " + date_time_str
    
    return date_time_str


def main():
    env = jinja2.Environment(loader=jinja2.FileSystemLoader("templates"))

    #render index.html
    render(env, "index.html")

    #render about-me/index.html
    edu_data_file = "materials/about-me/about-me-education.tsv"
    exp_data_file = "materials/about-me/about-me-experience.tsv"
    pub_data_file = "materials/about-me/about-me-publication.tsv"
    timeline_data_file = "materials/about-me/about-me-timeline.tsv"
    about_me_data = {}
    about_me_data["edu"] = read_tsv_data(edu_data_file)
    about_me_data["exp"] = read_tsv_data(exp_data_file)
    about_me_data["pub"] = read_tsv_data(pub_data_file)
    about_me_data["timeline"] = read_tsv_data(timeline_data_file)
    if not os.path.exists("about-me"):
        os.mkdir("about-me")
    shutil.copy("materials/about-me/fanghailing-photo.jpg", "about-me/fanghailing-photo.jpg")
    shutil.copy("templates/resume-cn.html", "about-me/resume-cn.html")
    render(env, "about-me.html", "about-me", about_me_data)

    #render life/index.html
    life_marks_file = "materials/life/life-marks.tsv"
    life_data = {}
    life_data["marks"] = read_tsv_data(life_marks_file)
    if not os.path.exists("life"):
        os.mkdir("life")
    if not os.path.exists("life/marks"):
        os.mkdir("life/marks")
    for line in life_data["marks"]:
        line[-1] = line[-1].split(";")
    for line in life_data["marks"]:
        pic_link_s = []
        mark_id, mark_date, mark_words, mark_pic_s = line
        mark_pic_dire = os.path.join("life/marks", "mark-" + mark_date + "-" + mark_id)
        if not os.path.exists(mark_pic_dire):
            os.mkdir(mark_pic_dire)
        for pic in mark_pic_s:
            dst_pic = os.path.join(mark_pic_dire, os.path.basename(pic))
            shutil.copy(pic, dst_pic)
            pic_link_s.append(os.path.join("/", dst_pic))
        line[-1] = pic_link_s
        line[1] = format_mark_data(mark_date)
    render(env, "life.html", "life", life_data)

    #render study/index.html
    render(env, "study.html", "study")

    #render documentation/index.html
    render(env, "documentation.html", "documentation")



if __name__ == "__main__":
    main()
