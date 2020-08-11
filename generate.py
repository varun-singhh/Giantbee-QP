from flask import Flask, render_template, make_response,request


app = Flask(__name__)


Q1 = []
im=[]
logo="xyx"
colname="xyx"
@app.route('/generate')
def generate():
	return render_template('form.html')


@app.route('/generate', methods=['post', 'get'])
def form_input():


    if request.method == 'POST':
        Q1.append(request.form.get('Q_1'))
        im.append(request.form.get('images'))
        l=request.form.get('logo')
        print(im)
        return render_template('form.html')

@app.route('/index') 
def pdf_template():
	
	return render_template('pdf_template.html',Q1=Q1,x=len(Q1),im=im,y=len(im),colname=colname,logo=logo,head=head,mark=mark)
@app.route('/new',) 
def new():
	Q1.clear()
	im.clear()
	return render_template('form.html')

@app.route('/log',methods=['post', 'get']) 
def log():
	if request.method == 'POST':
		global colname
		global logo
		global head
		global mark
		colname=request.form.get('colname')
		logo=request.form.get('logo')
		head=request.form.get('head')
		mark=request.form.get('mark')
		return render_template('form.html',c=colname,l=logo)
	return render_template('front.html')
if __name__ == '__main__':
	app.run(debug=True)
