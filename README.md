# Django REST Frameworkチュートリアル

仕事でDjango REST Frameworkを使ったので、チュートリアルみたいなものを書き残しておきます。

## Django REST Frameworkとは

DjangoでRESTful APIを実現するフレームワークです。略称は`DRF`。

公式サイト: <https://www.django-rest-framework.org/>

## 必要最小限のチュートリアル

まず全体の流れを知ってもらうために、必要最小限のチュートリアルを作成してみましょう。

### プロジェクト作成

`drf_tutorial`という名前でプロジェクトを作成します。
パッケージマネージャは何でもいいですが、今回は`poetry`を使います。

```sh
mkdir drf_tutorial
cd drf_tutorial
poetry init # すべてEnterでOK
poetry add django djangorestframework
poetry run django-admin startproject app . # .を忘れずに
poetry run django-admin startapp user
```

Django本体とDjango REST Frameworkを導入し、`app`プロジェクトを作成し、その中に`user`アプリケーションを作成しました。

終わったらプロジェクトにDRFと`user`アプリケーションを追加します。

`app/settings.py`

```python
# ...
INSTALLED_APPS = [
    # ...
    'rest_framework',
    'user',
]
```

ディレクトリ構成は以下のようになります。

```sh
.
├── app
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── poetry.lock
├── pyproject.toml
└── user
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py
```

### Model

APIのベースとなるのがModelです。それ以外の部分はDRFが面倒を見てくれるので楽なのですが、Modelだけはしっかり設計しなければなりません。

DRFとして特別な部分はなく、DjangoのModelと同じように作成します。

`user/models.py`

```python
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100, help_text='名前')
    birth_date = models.DateField(null=True, blank=True, help_text='誕生日')
    created_at = models.DateTimeField(auto_now_add=True, help_text='作成日時')
    updated_at = models.DateTimeField(auto_now=True, help_text='更新日時')
```

`User`Modelを作成しました。`help_text`を設定しておくとDRFがラベルなどに自動で使ってくれます。

Modelを作成したらマイグレーションを実行しておきます。

```sh
poetry run ./manage.py makemigrations
poetry run ./manage.py migrate
```

### Serializer

Serializerは、ModelからAPI用のJSONへの変換、また、APIに送られたJSONからModelへの逆変換を行います。

`user/serializers.py`

```python
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
```

`fields`はシリアライズ対象のフィールドを列挙します。`'__all__'`ですべてのフィールドが対象になります。

### View

ViewはDjangoのViewと同じ役目を果たすものです。HTTPのRequestを受けてResponseを返します。

`user/views.py`

```python
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
```

ViewSetは新規作成・一覧・取得・更新・削除のViewを一括で作成してくれます。

### Router

URLのルーティングを行う部分です。

`app/urls.py`

```python
from django.urls import include, path
from rest_framework import routers
from user.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
```

こちらもDRFが新規作成・一覧・取得・更新・削除のルーティングを一括で作成してくれます。
