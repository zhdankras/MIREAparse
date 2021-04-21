import xlrd

path = "ИИТ_3к_20-21_весна.xlsx"

inputWorkbook = xlrd.open_workbook(path)
inputWorksheet = inputWorkbook.sheet_by_index(0)

''' Разбиение пар на дни недели '''
def split_discipline(arr, size):
	arrs = []
	while len(arr) > size:
		pice = arr[:size]
		arrs.append(pice)
		arr = arr[size:]
	arrs.append(arr)
	return arrs

''' Запись данных в словарь '''
def write_to_dict():
	i = t = 0
	sp = []
	Rasp = {}
	while i < inputWorksheet.ncols-1:
		i+=5
		t+=1
		if t % 4 == 0:
			continue
		sp_of_discipline = []
		for a in inputWorksheet.col_values(i, 3, 75):
			sp_of_discipline.append(a)
		Rasp[inputWorksheet.cell_value(1, i)] = split_discipline(sp_of_discipline, 12)
	sp.append(Rasp)
	return sp

#print(inputWorksheet.cell_value2(2, 5))
A = write_to_dict()[0].get("ИКБО-05-18")