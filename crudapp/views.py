from django.shortcuts import render, get_object_or_404, redirect
from .forms import BoardForm
from .models import Board
from django.utils import timezone
from django.shortcuts import render

def main(request): # url로 요청할 경우 request로 받음
    boards = Board.objects
    return render(request, 'main.html', {'boards' : boards}) # html를 rendering 한 값을 return 

def board(request):
    if request.method == "POST":
        form = BoardForm(request.POST) # BoardForm으로 부터 받은 데이터를 처리하기 위한 인스턴스 생성
        if form.is_valid(): # 폼 검증 메소드
            board = form.save(commit = False) # board 오브젝트를 form으로 부터 가져오지만, 실제로 DB 반영은 하지 않는다.
            board.update_date = timezone.now()
            board.save()
            return redirect('main') # url의 name을 경로대신 입력한다.
        
    else:
        form = BoardForm() # forms.py의 BoardForm 클래스의 인스턴스
        return render(request, 'board.html', {'form' : form})
    return render(request, 'board.html')
    
def detail(request, pk):
    board_detail = get_object_or_404(Board, pk=pk)
    return render(request, "detail.html", {"board": board_detail})

def update(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == "POST":
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            board = form.save(commit=False)
            board.update_date = timezone.now()
            board.save()
            return redirect("main")
    else:
        form = BoardForm(instance=board)
        return render(request, "board.html", {"form":form})

def delete(request, pk):
    board = Board.objects.get(id=pk)
    board.delete()
    return redirect("main")