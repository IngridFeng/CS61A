; Lab 13: Final Review - Optional Questions

; Q5
(define (compose-all funcs)
  (define (composed x)
    (if
      (null? funcs)
        x
        (begin
          (define f (car funcs))
          (set! funcs (cdr funcs))
          (composed (f x))
          )
        )
      )
  composed
)

; Q6
(define (deep-map fn s)
  (cond
    ((null? s) nil)
    ((list? (car s)) (cons (deep-map fn (car s)) (deep-map fn (cdr s))))
    (else (cons (fn (car s)) (deep-map fn (cdr s))))
    )
)

; Q7
; Feel free to use these helper procedures in your solution
(define (map fn s)
  (if (null? s) nil
      (cons (fn (car s))
            (map fn (cdr s)))))

(define (filter fn s)
  (cond ((null? s) nil)
        ((fn (car s)) (cons (car s)
                            (filter fn (cdr s))))
        (else (filter fn (cdr s)))))

; Implementing and using these helper procedures is optional. You are allowed
; to delete them.
(define (unique s)
  (if
    (null? s)
      nil
      (cons (car s) (filter (lambda (x) (not (eq? x (car s)))) (unique (cdr s))))
    )
)

(define (count name s)
  (define (count-one name s)
    (if
      (null? s)
        0
        (+ 1 (count name (cdr s)))
      ))
  (count-one name (filter (lambda (x) (eq? x name)) s))
)

(define (tally names)
  (map (lambda (x) (cons x (count x names))) (unique names))
)

; Q8
(define (insert n s)
  (define (helper n s lst)
    (cond
      ((or (null? s) (<= n (car s))) (append lst (cons n s)))
      (else (helper n (cdr s) (append lst (list (car s)))))
      )
  )
  (helper n s nil)
)
