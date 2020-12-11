from flask import Flask, jsonify, request, redirect,url_for, render_template
import json


app = Flask(__name__)

@app.route('/predict_model', methods=['POST'])
def predict_model():

    data_dict=request.get_json(force=True)
    utrac_summary = [data_dict['summary']]
    utrac_detail =  [data_dict['detail']]
    utrac_response = [data_dict['comment']] #回覆
    utrac_value = [data_dict['value']]
    utrac_id = [data_dict['utrac_id']] # utrac單號
    utrac_recorder=[data_dict['logged_by']] #填單人員
    utrac_sentence = [data_dict['summary']+' '+data_dict['detail']+' '+data_dict['comment']]
    recorder_lst=[3967, 3202, 1031]
    #秀蘭-3967, 偉豪-3202, 信銘-1031

    
    if utrac_recorder[0] in recorder_lst:
     
        return '1, 提供確認頁面'
    else:
        return '1'


if __name__ == '__main__':
    app.run(debug=True)