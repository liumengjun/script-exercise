import appuifw, e32

def cn(x): return x.decode('utf-8')
appuifw.app.body=appuifw.Text()
appuifw.app.body.set(cn('hello world'))

e32.Ao_lock().wait()