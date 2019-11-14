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
convertToMorse([],[]).
convertToMorse(Text,Morse):-morse(Text,Morse).
convertToMorse([H|T],[Curr|Prev]):-morse(H,Curr),convertToMorse(T,Prev).
convertToMorse(Text,Morse):-
    atom_chars(Text, CharList),
    convertToMorse(CharList,Morse).

smorseToText('','').
smorseToText(Morse,Text):-morse(Text,Morse).
smorseToText(Smorse,[Text|Prev]):-
    sub_string(Smorse,0,Length,_,Substring),
    morse(Text,Substring),
    sub_string(Smorse,Length,_,0,Next),
    smorseToText(Next,Prev).



