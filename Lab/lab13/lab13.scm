; Lab 13: Final Review

; Q2
(define (rle s)
  (define (runs val s count)
    (cond
      ((null? s) (cons-stream (list val count) nil))
      ((= val (car s)) (runs (car s) (cdr-stream s) (+ 1 count)))
      (else (cons-stream (list val count) (runs (car s) (cdr-stream s) 1)))
      )
      )
    (if
      (null? s)
        nil
        (runs (car s) (cdr-stream s) 1)
    )
)

; Q2 testing functions
(define (list-to-stream lst)
    (if (null? lst) nil
                    (cons-stream (car lst) (list-to-stream (cdr lst))))
)

(define (stream-to-list s)
    (if (null? s) nil
                 (cons (car s) (stream-to-list (cdr-stream s))))
)

; Q3
(define (tail-replicate x n)
  (define (rep x n lst)
    (cond
      ((= n 0) lst)
      (else (rep x (- n 1) (cons x lst)))
      )
  )
  (rep x n nil)
)
