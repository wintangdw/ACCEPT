import csv
import smtplib
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_sender = str(input("Please input your email: "))
password = getpass.getpass("Please input your password: ")
subject = "Informasi Actuarial Exam Preparation (ACCEPT) "

with open('receiver-list.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        text = """"""
        text += "Halo teman-teman sperjuangan aktuaris!\n\n"
        text += "Terimakasih telah mendaftarkan diri Anda di Actuarial Wxam Preparation (ACCEPT). Berikut kami sampaikan username dan password Anda (informasi ini pribadi, harap tidak memberi tahu pihak manapun\n\n"
        text += "Username: {}\n".format(line[1])
        text += "Password: {}\n\n".format(line[2])
        text += "Berikut beberapa informasi tambahan terkait pengerjaan try out ACCEPT:\n"
        text += "   A. Langkah-langkah pengerjaan try out:\n"
        text += "       1. Kunjungi website cbt.ipb.ac.id\n"
        text += "       2. Masukkan username dan password yang kami berikan di email ini\n"
        text += "       3. Ganti password Anda dengan password baru yang Anda buat\n"
        text += '       4. Anda akan diarahkan ke dashboard yang berisi course yang dapat Anda kerjakan. Pilihlah course "Actuarial Exam Preparation"\n'
        text += "       5. Anda dapat mengerjakan try out sesuai mata uji yang Anda pilih pada saat registrasi\n"
        text += "   B. Sebagai persiapan tambahan, kami mengadakan simulasi pengerjaan try out pada:\n"
        text += "       Hari, tanggal   : Kamis, 2 Juni 2022\n"
        text += "       Waktu           : 08..00 - 22.00 WIB (Waktu pengerjaan fleksibel)\n"
        text += "       Semua peserta diwajibkan mengerjakan simulasi (nilai simulasi tidak memengaruhi penilaian akhir). Langkah-langkah pengerjaan simulasi sama dengan poin A.\n"
        text += "   C. Bagi peserta yang belum memasuki grup, silahkan bergabung di grup Whatsapp berikut ini:\n"
        text += "       https://ipb.link/grup-accept-2022\n"
        text += "   D. Untuk penjelasan lebih rinci mengenai langkah-langkah pengerjaan try out ACCEPT, dapat ditonton pada video dengan tautan sebagai berikut:\n"
        text += "       https://ipb.link/tutorial-accept-2022\n\n"
        text += "Apabila Anda mengalami kendala terkait login atau pengerjaan soal, silahkan bertanya di grup peserta atau Anda bisa menghubungi cp yang tertera berikut:\n"
        text += "081927648355 (Farah)\n\n\n"
        text += '"Persiapan hari ini menentukan pencapaian hari esok"\n'
        text += "Semangat mengerjakan ujian\n"
        email_send = line[0]
        msg = MIMEMultipart()
        msg['From'] = email_sender
        msg['To'] = email_send
        msg['Subject'] = subject
        msg.attach(MIMEText(text, "plain"))
        text = msg.as_string()

        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(email_sender, password)
        server.sendmail(email_sender, email_send, text)

        server.quit


