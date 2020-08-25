from flask import Flask
app = Flask(__name__)

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

@app.route('/')
def hello_world():
    # Пример дебагинга
    print('Успешно стартовал')
    return '<h1>Hello, World and LeSS SUPERRR!</h1>'

# Передача переменной из браузера в файл
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    print('Обрабатываю переменную - username', username)
    return 'UseR %s' % username

# Передача переменной из браузера в файл
@app.route('/avg/<numbers>')
def show_avg(numbers):
    # show the user profile for that user
    nums = numbers.split(',')
    nums = [float(num)for num in nums ]
    mean_nums = mean(nums)
    print(nums, ' mean=', mean_nums)
    return ('<h3>'+str(nums)+' mean='+ str(mean_nums)+'</h3>')

@app.route('/iris')
def show_iris():
    from sklearn.datasets import load_iris
    data = load_iris()
    data.target[[10, 25, 50]]
    ret = list(data.target_names)
    return (str(ret))