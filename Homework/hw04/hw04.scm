; Q1
(define (sign x)
  (cond
    ((< x 0) -1)
    ((= x 0) 0)
    (else 1)
    )
)

; Q2
(define (square x) (* x x))

(define (pow b n)
  (cond
    ((= n 0) 1)
    ((= n 1) b)
    ((even? n) (square (pow b (/ n 2))))
    ((odd? n) (* b (square (pow b (/ (- n 1) 2)))))
    )
)

; Q3
(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)

; Q4
(define (ordered? s)
  (cond
    ((null? (cdr s)) #t)
    ((<= (car s) (cadr s)) (ordered? (cdr s)))
    (else #f)
    )
)

; Q5
(define (nodots s)
  (cond
   ((null? s) s)
   ((and (pair? (car s)) (number? (cdr s))) (cons (nodots (car s)) (cons (cdr s) ())))
   ((number? (cdr s)) (cons (car s) (cons (cdr s) ())))
   ((pair? (car s)) (cons (nodots (car s)) (nodots (cdr s))))
   (else (cons (car s) (nodots (cdr s))))
   )
)

; Q6
(define (empty? s) (null? s))

(define (add s v)
  (cond
    ((empty? s) (list v))
    ((< v (car s)) (cons v s))
    ((= v (car s)) s)
    ((> v (car s)) (cons (car s) (add (cdr s) v)))
    )
)

; Q7
; Sets as sorted lists
(define (contains? s v)
  (define added (add s v))
  (define (compare x y)
    (cond
      ((empty? x) (empty? y))
      ((= (car x) (car y)) (compare (cdr x) (cdr y)))
      (else #f)
      )
    )
  (compare added s)
)

; Q8
(define (intersect s t)
  (cond
    ((or (empty? s) (empty? t)) ())
    ((contains? s (car t)) (cons (car t) (intersect s (cdr t))))
    (else (intersect s (cdr t)))
    )
)

(define (union s t)
  (if (empty? t) s (union (add s (car t)) (cdr t))))
)
