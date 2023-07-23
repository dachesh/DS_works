# Split and compare strings
# Challenge 1: split a paragraph

para = """From the corner of the divan of Persian saddle-bags on which he was lying, smoking, as was his custom, innumerable cigarettes, Lord Henry Wotton could just catch the gleam of the honey-sweet and honey-coloured blossoms of a laburnum, whose tremulous branches seemed hardly able to bear the burden of a beauty so flame-like as theirs; and now and then the fantastic shadows of birds in flight flitted across the long tussore-silk curtains that were stretched in front of the huge window, producing a kind of momentary Japanese effect, and making him think of those pallid jade-faced painters of Tokio who, through the medium of an art that is necessarily immobile, seek to convey the sense of swiftness and motion. The sullen murmur of the bees shouldering their way through the long unmown grass, or circling with monotonous insistence round the dusty gilt horns of the straggling woodbine, seemed to make the stillness more oppressive. The dim roar of London was like the bourdon note of a distant organ."""
arr1 = para.split('.')
#print(len(arr1))

for item in range(len(arr1)):
	print(item)
	
	arr_item = arr1[item]
	arr2 = arr_item.split()
	arrset = list(set(arr2))
	temp = []
	temp.append(arrset)
	#print(type(arr_item))
