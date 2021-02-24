# Git Commit Rule

**- Git Commit Rule을 꼭 지켜주세요!**
 >- Git Commit Rule은 앞으로 여러분께서 다른 오픈소스에 컨트리뷰트하실 때에도 꼭 지켜주셔야 하는 하나의 약속입니다.
 >- Git Commit Rule은 오픈소스 레포지토리마다 조금씩 상이할 수 있으나, 큰 틀에서는 똑같습니다.
 >- 하나의 커밋을 올릴 때마다, Web IDE에서 제공하는 기본 메시지(Github에서 기본으로 제공하는 메시지)를 사용하지 말고, 꼭 그 부분을 아래와 같은 포맷으로 채워주세요.

**Git Commit Rule의 기본**
 >- Git Commit Rule의 기본 뼈대는 아래와 같습니다.
    <pre><code>Type: Subject<br>
body<br>
footer</code></pre>

**Type의 구성 요소**
 >- Type에서는 아래의 7가지만 사용하실 수 있습니다.
    <pre><code>- feat 		: 새로운 기능 추가
    - fix 		: 버그 수정
    - docs 		: 문서 수정
    - style 	: 코드 formatting, 세미콜론(;) 누락, 코드 변경이 없는 경우
    - refactor 	: 코드 리팩토링
    - test 		: 테스트 코드, 리팽토링 테스트 코드 추가
    - chore 	: 빌드 업무 수정, 패키지 매니저 수정</code></pre>

**Subject(제목)**
- 제목은 아래 Rule을 상기해주세요!
 >- 제목은 50자를 넘기지 않고, 마침표를 붙이지 않습니다.
 >- 제목에는 위 커밋 종류를 함께 씁니다.
 >- 과거시제를 사용하지 않고 명령조로 작성합니다.
 >- 제목과 본문은 한 줄 띄워 분리합니다.
 >- 제목의 첫 글자는 반드시 대문자로 씁니다.
 >- 제목이나 본문에 이슈 번호(가 있다면) 붙여야 합니다.

**Body(본문)**
- 본문에는 조금 더 자유롭게 쓰실 수 있어요.
 >- 선택사항이기에 모든 커밋에 본문 내용을 작성할 필요는 없습니다.
 >- 한 줄에 72자를 넘기면 안됩니다.
 >- 어떻게(How)보다 무엇을, 왜(What, Why)에 맞춰 작성합니다.
 >- 설명뿐만 아니라, 커밋의 이유를 작성할 때에도 씁니다.
 >- Git CLI tool(커맨드라인 툴) 활용 시에는 자동적으로 따라붙지만, Digital Signage(`Signed-off-by: underflow101 <ikarus125@gmail.com>`)를 꼭 첨부해주셔야해요. (해당 PR에 대해 자신이 책임을 지는 모습이에요 :D)

**Footer(꼬리말) [Optional]**
- 꼬리말은 어떤 PR이나 Issue를 명기하고 싶을 때만 쓰세요.
 >- 선택사항이기에 모든 커밋에 꼬릿말을 작성할 필요는 없습니다.
 >- Issue Tracker ID를 작성할 때 사용합니다.
 >- Example)
    <pre><code>Resolves: #123
    See also: #456, #789</pre></code>

### Example
<pre><code>feat: Add 'Go to SOS-Masters Homepage' Button

- Added 'Go to SOS-Masters Homepage' Button
    - This will link users to SOS-Masters Homepage URL
    - If user clicks this button, web browser will automatically pop up.

Resolves: #2

Signed-off-by: underflow101 <ikarus125@gmail.com> </code></pre>