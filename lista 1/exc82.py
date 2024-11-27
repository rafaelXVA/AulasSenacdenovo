def dias_entre_datas(data1, data2):
    def data_para_dias(data):
        dia, mes, ano = map(int, data.split('/'))
        dias_no_ano = (ano - 1) * 365  
        dias_no_ano += (ano - 1) // 4  
        dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        dias_no_mes = sum(dias_por_mes[:mes - 1])
        return dias_no_ano + dias_no_mes + dia
    dias_data1 = data_para_dias(data1)
    dias_data2 = data_para_dias(data2)
    return abs(dias_data1 - dias_data2)
data1 = "9/11/2024"
data2 = "11/11/2024"
print(dias_entre_datas(data1, data2))