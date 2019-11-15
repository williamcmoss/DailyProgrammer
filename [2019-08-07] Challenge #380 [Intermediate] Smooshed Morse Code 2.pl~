morse('a','.-').
morse('b','-...').
morse('c','-.-.').
morse('d','-..').
morse('e','.').
morse('f','..-.').
morse('g','--.').
morse('h','....').
morse('i','..').
morse('j','.---').
morse('k','-.-').
morse('l','.-..').
morse('m','--').
morse('n','-.').
morse('o','---').
morse('p','.--.').
morse('q','--.-').
morse('r','.-.').
morse('s','...').
morse('t','-').
morse('u','..-').
morse('v','...-').
morse('w','.--').
morse('x','-..-').
morse('y','-.--').
morse('z','--..').

convertList([],[]).
convertList(Text,Morse):-morse(Text,Morse).
convertList([H|T],[Curr|Prev]):-morse(H,Curr),convertList(T,Prev).

textToMorse(Text,Morse):-
    atom_chars(Text,TextList),
    convertList(TextList, MorseList),
    atomic_list_concat(MorseList, Morse).

morseToText(Curr,Morse):-
    sub_atom(Morse,0,Length,_,CurrMorse),
    morse(Curr,CurrMorse),
    sub_atom(Morse,Length,0,0,'').
morseToText(Sum,Morse):-
    sub_atom(Morse,0,Length,_,CurrMorse),
    morse(Curr,CurrMorse),
    sub_atom(Morse,Length,_,0,PrevMorse),
    morseToText(Prev,PrevMorse),
    atom_concat(Curr,Prev,Sum).






