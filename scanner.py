"""
Sample script to test ad-hoc scanning by table drive.
This accepts a number with optional decimal part [0-9]+(\.[0-9]+)?

NOTE: suitable for optional matches
"""




def getchar(text,pos):
	""" returns char category at position `pos` of `text`,
	or None if out of bounds """
	
	if pos<0 or pos>=len(text): return None
	
	c = text[pos]
	
	# **Σημείο #3**: Προαιρετικά, προσθέστε τις δικές σας ομαδοποιήσεις
	
	#if c>='0' and c<='9': return 'DIGIT'	# 0..9 grouped together
	
	#if c=='.': return 'DOT'	# dot as a category by itself
	
	return c	# anything else
	


def scan(text,transitions,accepts):
	""" scans `text` while transitions exist in
	'transitions'. After that, if in a state belonging to
	`accepts`, it returns the corresponding token, else ERROR_TOKEN.
	"""
	
	# initial state
	pos = 0
	state = 's0'
	# memory for last seen accepting states
	last_token = None
	last_pos = None
	
	
	while True:
		
		c = getchar(text,pos)	# get next char (category)
		
		if state in transitions and c in transitions[state]:
			state = transitions[state][c]	# set new state
			pos += 1	# advance to next char
			
			# remember if current state is accepting
			if state in accepts:
				last_token = accepts[state]
				last_pos = pos
			
		else:	# no transition found

			if last_token is not None:	# if an accepting state already met
				return last_token,last_pos
			
			# else, no accepting state met yet
			return 'ERROR_TOKEN',pos
			
# **Σημείο #1**: Αντικαταστήστε με το δικό σας λεξικό μεταβάσεων	
transitions = {	'q0': {'1': 'q1', '2': 'q1', '3': 'q2'},
						'q1': {'1': 'q5','2': 'q5','3': 'q5','4': 'q5','5': 'q5','6': 'q5','7': 'q5','8': 'q5','9': 'q5','0': 'q5'},
						'q2': {'1': 'q3','2': 'q3','3': 'q3','4': 'q3','5': 'q4'},
						'q3': {'1': 'q6','2': 'q6','3': 'q6','4': 'q6','5': 'q6','6': 'q6','7': 'q6','8': 'q6','9': 'q6','0': 'q6'},
						'q4': {'0': 'q6'},
						'q5': {'1': 'q6','2': 'q6','3': 'q6','4': 'q6','5': 'q6','6': 'q6','7': 'q6','8': 'q6','9': 'q6','0': 'q6'},
						'q6': {'1': 'q7','2': 'q7','3': 'q7','4': 'q7','5': 'q7','6': 'q7','7': 'q7','8': 'q7','9': 'q7','0': 'q7'},
						'q7': {'1': 'q8','2': 'q8','3': 'q8','4': 'q8','5': 'q8','6': 'q8','7': 'q8','8': 'q8','9': 'q8','0': 'q8'},
						'q8': {'K': 'q9','M': 'q11'},
						'q9': {'T': 'q10'},
						'q11': {'P': 'q12'}	,	
						'q12': {'S': 'q13'}

					}
# **Σημείο #2**: Αντικαταστήστε με το δικό σας λεξικό καταστάσεων αποδοχής# **Σημείο #2**: Αντικαταστήστε με το δικό σας λεξικό καταστάσεων αποδοχής
accepts = {	'q13' : 'MPS_TOKEN',
				'q10': 'KT_TOKEN'
				}


# get a string from input
text = input('give some input>')

# scan text until no more input
while text:		# i.e. len(text)>0
	# get next token and position after last char recognized
	token,pos = scan(text,transitions,accepts)
	if token=='ERROR_TOKEN':
		print('unrecognized input at position',pos,'of',text)
		break
	print("token:",token,"text:",text[:pos])
	# new text for next scan
	text = text[pos:]
	
