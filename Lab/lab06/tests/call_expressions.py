test = {
  'name': 'Call Expressions',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from operator import add
          >>> def double(x):
          ...     return x + x
          >>> def square(y):
          ...     return y * y
          >>> def f(z):
          ...     add(square(double(z)), 1)
          >>> f(4)
          75e7eb45dffa5d30654f02570401dfe8
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def foo(x, y):
          ...     print("x or y")
          ...     return x or y
          >>> a = foo
          75e7eb45dffa5d30654f02570401dfe8
          # locked
          >>> b = foo()
          34db8258c24aff02f4e0aeaa32af407b
          # locked
          >>> c = a(print("x"), print("y"))
          375e66c69b9732d25b7216fbdb627aa2
          71ee8177f4716fe5f13cb6a14055993c
          8de8ba3c13511f7a2ef3db91eed0c745
          # locked
          >>> print(c)
          9e7a96d3ae4b4ef7cb85e10bcc434b41
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def welcome():
          ...     print('welcome to')
          ...     return 'hello'
          >>> def cs61a():
          ...     print('cs61a')
          ...     return 'world'
          >>> print(welcome(), cs61a())
          eca09dd9733c5803e96b31d8cf34e9f6
          6f4a01654edbca7bcfc1774aef141d8b
          a14af83d9c3dcc07ff4a1a830e6b3d81
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
