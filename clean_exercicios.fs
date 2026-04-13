\ Exercícios de Forth - Versão limpa para testes

\ sort-two ( a b -- x y )
\ Coloca os dois números em ordem crescente
: sort-two
    2dup < if swap then
;

\ sort-three ( a b c -- x y z )
\ Coloca os três números em ordem crescente usando sort-two
: sort-three
    sort-two
    2dup rot
    sort-two
    rot sort-two
;

\ dots ( n -- )
\ Imprime uma linha com n pontos
: dots
    0 do
        ." ."
    loop
    cr
;

\ ** ( a b -- a^b )
\ Eleva a à potência b (assumindo b >= 0)
: **
    1 swap 0 do
        over *
    loop
    swap drop
;

\ 3dup ( a b c -- a b c a b c )
\ Duplica os três números do topo da pilha
: 3dup
    2 pick 2 pick 2 pick
;

\ put ( ... a n -- ... a ... )
\ Coloca a na posição n da pilha
: put
    dup 0= if
        drop
    else
        dup 1= if
            drop swap
        else
            1- swap
            rot rot
            put
            swap
        then
    then
;

\ reverse ( ... n -- ... )
\ Inverte a ordem dos últimos n números da pilha
: reverse
    0 do
        1- pick
    loop
    0 do
        swap
    loop
;

\ drop-many ( ... n -- ... )
\ Remove os últimos n números da pilha
: drop-many
    0 do
        drop
    loop
;

\ drop-at ( ... n -- ... )
\ Remove o número na posição n da pilha
: drop-at
    dup 0= if
        drop
    else
        dup 1= if
            drop drop
        else
            1- swap
            rot rot
            drop-at
            swap
        then
    then
;

\ pop-at ( ... n -- ... a )
\ Move o valor na posição n para o topo da pilha
: pop-at
    dup 0= if
        drop
    else
        dup 1= if
            drop swap
        else
            1- swap
            rot rot
            pop-at
            swap
        then
    then
;

\ print-change ( a -- )
\ Imprime a quantidade de notas e moedas para compor o valor
: print-change
    dup 100 / dup ."  nota(s) de 100" cr
    swap 100 mod dup 50 / dup ."  nota(s) de 50" cr
    swap 50 mod dup 20 / dup ."  nota(s) de 20" cr
    swap 20 mod dup 10 / dup ."  nota(s) de 10" cr
    swap 10 mod dup 5 / dup ."  nota(s) de 5" cr
    swap 5 mod dup 2 / dup ."  nota(s) de 2" cr
    swap 2 mod dup 1 / ."  moeda(s) de 1" cr
    drop drop drop drop drop drop
;

\ max-n ( ... n -- max )
\ Deixa apenas o maior de n números na pilha
: max-n
    dup 0= if
        drop
    else
        1- swap
        max-n
        swap max
    then
;

\ reset ( ... -- )
\ Remove todos os números da pilha
: reset
    depth 0 do
        drop
    loop
;

\ all-positive ( ... -- flag )
\ Verifica se todos os números na pilha são positivos
: all-positive
    depth 0= if
        -1 \ true
    else
        depth 1- roll
        dup 0< if
            drop reset 0 \ false
        else
            all-positive
        then
    then
;

\ all-sorted ( ... -- flag )
\ Verifica se os números estão em ordem crescente
: all-sorted
    depth 2 < if
        -1 \ true
    else
        depth 2 - roll
        depth 1 - roll
        over > if
            drop drop reset 0 \ false
        else
            -rot all-sorted
        then
    then
;

\ filter-positive ( ... -- ... )
\ Deixa apenas os números positivos na pilha (incluindo zero)
: filter-positive
    depth 0= if
    else
        depth 1 - roll
        dup 0>= if
        else
            drop
        then
        filter-positive
    then
;
