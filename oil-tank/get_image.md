
Let's pick a text with an acronym:

`text="Pep Guardiola, NBA & NFL helped turn England into potential world champions"`{{execute}}

Simple dictionary:

`abbrevs={'NBA':'National Basketball Association','NFL':'National Football League'}
for abbrev in abbrevs:
    text= text.replace(abbrev,abbrevs[abbrev])`{{execute}}
    
Let's see how it was normalized:
`print(text)`{{execute}}
