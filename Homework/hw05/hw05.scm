;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Mutable functions in Scheme

(define (make-fib)
  (define curr 0) (define next 1)
  (define count 0)
  (lambda ()
    (if (= count 0) (set! count (+ count 1))
      (begin
      (define tmp next)
      (set! next (+ curr next))
      (set! curr tmp)
      ))
      curr)
  )
