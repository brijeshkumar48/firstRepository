from django.shortcuts import render
from .models import *
from django.http.response import HttpResponse, JsonResponse, StreamingHttpResponse
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
import xlsxwriter
import os
import base64
import datetime
import qrcode
# Create your views here.

def personDetails(request):
    user_details = Peron.objects.filter(id=1).first()
    person_data = user_data(user_details)

    qr_path = qrCode(request)
    media_url = f"{settings.MEDIA_ROOT}" + "qr_codes/"
    dqrCodePath = media_url + user_details.qrCode
    with open(dqrCodePath, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        data = encoded_string.decode("utf-8")
        qrBase64 = f"data:image/png;base64,{data}" 
    
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['Subject']
        message = request.POST['message']
        ContactUs.objects.create(name=name,email=email,subject=subject,message=message)
        

    return render(request, "userProfile/details.html",{"person_data":person_data, "qrCode":qrBase64})


def download(request):
    user_details = Peron.objects.filter(id=1).first()
    resp = f"{settings.MEDIA_ROOT}" + str(user_details.pdf)
    with open(resp, 'rb') as pdf:
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'filename=brijesh_resume.pdf'
        return response


def excelData(request):
    user_details = Peron.objects.filter(id=1).first()
    person_data = user_data(user_details)
    dateTime = datetime.datetime.now()
    dateTimeNow = dateTime.strftime("%d-%m-%Y_%H.%M.%S")
    fileName = "brijesh_resume_data" + '_' + str(dateTimeNow)

    folder_name = "brijesh_resume"
    media_url = f"{settings.MEDIA_ROOT}"
    directory = media_url + folder_name
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_path = directory + "/" + fileName + "." + 'xlsx'

    workbook = xlsxwriter.Workbook(file_path)
    worksheet = workbook.add_worksheet('resume_data')

    header_format = workbook.add_format({'bold': True,'bottom': 2,'valign': 'vcenter','bg_color': '#F9DA04','text_wrap': True,'border':1, 
                                        'border_color':'black', 'align': 'center','color':'red'})

    header3_format = workbook.add_format({'bold': True,'bottom': 2,'valign': 'vcenter','text_wrap': True,'border':1, 'border_color':'black',                
                                        'align':'center'})

    cell_format = workbook.add_format({'text_wrap': True,'border_color':'black','align': 'center'})

    worksheet.set_column('A:A', 13), worksheet.set_column('B:B', 12), worksheet.set_column('C:C', 13), worksheet.set_column('D:D', 25), 
    worksheet.set_column('E:E', 20), worksheet.set_column('F:F', 13), worksheet.set_column('G:G', 12), worksheet.set_column('H:H', 25), worksheet.set_column('I:I', 25), worksheet.set_column('J:J', 20), worksheet.set_column('K:K',30), worksheet.set_column('M:M', 25), worksheet.set_column('N:N', 25)

    header3_data = ['Name', 'Gender', 'Mobile Number','Email','Address','Title','Education','Edu. Name','University Name','Percentage','Employer Name','Location','Current Designation','Duration','Salary']
    for col_num, data in enumerate(header3_data):
        worksheet.write(1, col_num, data, header3_format)

    cell_format.set_align('vcenter')
    worksheet.set_default_row(30)

    resume_data = "RESUME DATA" 
    worksheet.merge_range("A1:O1",  resume_data,header_format)


    count = 0
    team_count = 0
    row_number = 3
    edu_row_number = 3
    org_col_number = 10
    edu_col_number = 6

    person_data = [person_data]
    for items in person_data:
        if items:
            team_count +=1
            count = len(items['organization_details']) - 1                
            worksheet.merge_range(f'A{row_number}:A{row_number+count}', items['name'], cell_format)
            worksheet.merge_range(f'B{row_number}:B{row_number+count}', items['gender'], cell_format)
            worksheet.merge_range(f'C{row_number}:C{row_number+count}', items['mobile_number'], cell_format)
            worksheet.merge_range(f'D{row_number}:D{row_number+count}', items['email'], cell_format)
            worksheet.merge_range(f'E{row_number}:E{row_number+count}', items['address'], cell_format)
            worksheet.merge_range(f'F{row_number}:F{row_number+count}', items['others'], cell_format)

            for detail in items['education_detail']:
                edu_row = edu_row_number
                worksheet.merge_range(f'G{edu_row}:G{edu_row+count}' , detail['short_name'],cell_format)
                worksheet.merge_range(f'H{edu_row}:H{edu_row+count}', detail['course_name'],cell_format)
                worksheet.merge_range(f'I{edu_row}:I{edu_row+count}', detail['university_name'],cell_format)
                worksheet.merge_range(f'J{edu_row}:J{edu_row+count}', detail['percentage'],cell_format)
                edu_row_number +=1

            for details in items['organization_details']:
                row = row_number -1
                worksheet.write(row, org_col_number, details['org_name'],cell_format)
                worksheet.write(row, org_col_number + 1, details['location'],cell_format)
                worksheet.write(row, org_col_number + 2, details['current_designation'],cell_format)
                worksheet.write(row, org_col_number + 3, details['duration'],cell_format)
                worksheet.write(row, org_col_number + 4, details['salary'],cell_format)
                row_number +=1


    workbook.close()

    if file_path:
        with open(file_path, 'rb') as excel:
            response = HttpResponse(excel.read(),content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            response['Content-Disposition'] = 'attachment; filename=brijesh_resume_data.xlsx'     
            return response


def qrCode(request):
    user_details = Peron.objects.filter(id=1).first()

    domain = request.META['HTTP_HOST']
    url = str(domain)+"/person-detail/excel_download/"
    data = url
    qr = qrcode.QRCode(version = 1,
                    box_size = 10,
                    border = 5)

    qr.add_data(data)
    qr.make(fit = True)
    img = qr.make_image(fill_color = 'black',
                        back_color = 'white')

    file_name = "brijesh_qr"
    folder_name = "qr_codes"
    media_url = f"{settings.MEDIA_ROOT}"
    directory = media_url + folder_name

    if not os.path.exists(directory):
        os.makedirs(directory)

    img.save(str(directory)+ "/" + file_name +'.png')

    obj_image_path = file_name +'.png'

    user_details.qrCode = obj_image_path
    user_details.save()   

    return obj_image_path 



def user_data(user_details):
    person_data = []
    if user_details:
        person_data = {
            "name": user_details.name,
            "gender": user_details.gender,
            "dob": user_details.dob,
            "mobile_number": user_details.mobile_number,
            "email": user_details.email,
            "address": user_details.address,
            "objective": user_details.objective,
            "others": user_details.others
        }

        organization_details = Organization.objects.filter(person_id=user_details.id)
        person_datas = []
        for organization in organization_details:
            person_data_list = {}
            person_data_list['org_name'] = organization.org_name
            person_data_list['location'] = organization.location
            person_data_list['current_designation'] = organization.current_designation
            person_data_list['salary'] = organization.salary
            person_data_list['projects'] = organization.projects
            person_data_list['work_description'] = organization.work_description
            person_data_list['duration'] = organization.duration

            person_datas.append(person_data_list.copy())

        education_details = Education.objects.filter(person_id=user_details.id)
        education_detail = []
        for education in education_details:
            education_details_list = {}
            education_details_list['course_name'] = education.course_name
            education_details_list['short_name'] = education.short_name
            education_details_list['university_name'] = education.university_name
            education_details_list['description'] = education.description
            education_details_list['completion_date'] = education.completion_date
            education_details_list['percentage'] = education.percentage

            education_detail.append(education_details_list.copy())

        cerification_details = Certification.objects.filter(person_id=user_details.id)
        cerification_detail = []
        for cerification in cerification_details:
            cerification_details_list = {}
            cerification_details_list['laungue_name'] = cerification.laungue_name
            cerification_details_list['institute_name'] = cerification.institute_name
            cerification_details_list['cert_description'] = cerification.cert_description

            cerification_detail.append(cerification_details_list.copy())


        skill_details = Skill.objects.filter(person_id=user_details.id)
        skill_detail = []
        for skill in skill_details:
            skill_details_list = {}
            skill_details_list['skill_name'] = skill.skill_name
            skill_details_list['perce_of_proficiency'] = skill.perce_of_proficiency

            skill_detail.append(skill_details_list.copy())

        person_data['organization_details']=person_datas
        person_data['education_detail']=education_detail
        person_data['cerification_detail']=cerification_detail
        person_data['skill_detail']=skill_detail

    return person_data

