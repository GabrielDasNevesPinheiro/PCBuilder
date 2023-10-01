# Você está dentro dos meus pensamentos agora

## Desenvolvendo `HardwareStatus.py` e `Certificate.py`
<div style="font-size: 1.3rem;">
    <p>Sim, se vai ler isso, vai acompanhar todo o meu pensamento durante a jornada do desenvolvimento</p>
    <p>Ainda não comecei a codar, estou preso aqui pensando na estrutura de pastas...</p>
    <p>Decidi colocar as classes dentro de src/models 😐</p>
    <p>Desenvolvendo a classe HardwareStatus tive a ideia de implementar um toString que me trouxesse um status em texto baseado em algum status da classe, vou fazer o mesmo com Certificate</p>
</div>

## Desenvolvendo `Component.py`
<div style="font-size: 1.3rem">
    <p>Pensei agora aqui em criar um construtor em Component.py, assim consigo user um super em todas as outras classes</p>
    <p> Após criar o corpo básico da classe percebi que é interessante eu implementar um toString em todas as classes.</p>
</div>

<div style="font-size: 1.3rem">
    <p></p>
</div>

## Desenvolvendo `Processor.py`
<div style="font-size: 1.3rem">
    <p>Agora vem algo interessante, veja, percebe que pensei em um método getTDP para todos os componentes que possuem um consumo de energia no sistema?</p>
    <p> então, o que irei fazer nesse método é uma lógica que calcula o consumo de energia baseado nos clocks, as proporções dos calculos vão variar de componente para componente</p>
    <p>O calculo que pensei aqui foi algo baseado em um multiplicador base para controlar o TDP final baseado no core clock do cpu, ao meu ver, ficou balanceado</p>
    <p>Começou a tocar sliver(nirvana) e acabei me distraindo cantando 😶</p>
</div>


## Desenvolvendo `RAM.py`
<div style="font-size: 1.3rem">
    <p>Percebi aqui que preciso implementar uma função para trocar a frequencia da RAM, mas não na classe RAM, isso é responsabilidade da placa mãe.</p>
</div>

## Desenvolvendo `Motherboard.py`
<div style="font-size: 1.3rem">
    <p>Decidi que ramSlots é um atributo apenas de inicialização, será apenas utilizado no construtor da classe para que a lista de slots de ram, no atributo ram seja o único atributo relacionado à memórias ram.</p>
    <p>Não criarei sobrecarga da função attach</p>
    <p>Pensei em implementar um status NO_VIDEO no HardwareStatus :)</p>
</div>

<p>Leia as letras miúdas sempre</p>
<p>No fim o sistema funciona mas o código tá muito bagunçado</p>
<p>Montei um hardware maluco e ele está em chamas</p>