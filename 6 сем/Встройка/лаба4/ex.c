1.	#include "RTE_Components.h" // Component selection
2.	#include CMSIS_device_header // Device header
3.	#include <stdio.h>
4.	
5.	static volatile uint32_t ui_cout100ms=0;
6.	
7.	void delay(void){
8.	    volatile uint32_t i=6000000;
9.	    while(i > 0)
10.	    i--;
11.	}
12.	
13.	int main(void) {
14.	    // Настройка частоты
15.	    uint32_t priGroup = 0, PreemptPriority=0, SubPriority=0;
16.	    //настройка частоты 72 МГц
17.	    SET_BIT(RCC -> CR,RCC_CR_HSEON);
18.	    while((RCC->CR & RCC_CR_HSERDY)==0){}
19.	    FLASH->ACR = FLASH_ACR_PRFTBE|FLASH_ACR_LATENCY_1;
20.	    RCC->CFGR |= (uint32_t)(RCC_CFGR_PLLSRC_HSE_PREDIV | RCC_CFGR_PLLMUL9);
21.	    SET_BIT(RCC -> CR,RCC_CR_PLLON);
22.	    while((RCC->CR & RCC_CR_PLLRDY) == 0){}
23.	    RCC->CFGR &= (uint32_t)((uint32_t)~(RCC_CFGR_SW));
24.	    RCC->CFGR |= (uint32_t)RCC_CFGR_SW_PLL;
25.	    while ((RCC->CFGR & (uint32_t)RCC_CFGR_SWS) != (uint32_t)RCC_CFGR_SWS_PLL){}
26.	    SystemCoreClockUpdate();//проверяем частоту SystemCoreClock
27.	    printf("clk=%d\n",SystemCoreClock);
28.	        
29.	    // Настройка кнопок
30.	    SET_BIT(RCC ->APB2ENR, RCC_APB2ENR_SYSCFGEN);//разрешаем тактиро-вание SYSCFG
31.	    SET_BIT(RCC -> AHBENR, RCC_AHBENR_GPIOCEN); //GPIOC
32.	        
33.	    CLEAR_BIT(GPIOC->MODER,GPIO_MODER_MODER0|GPIO_MODER_MODER3|GPIO_MODER_MODER4|GPIO_MODER_MODER5); //PC0,3,4,5 In
34.	    SET_BIT(GPIOC->PUPDR,GPIO_PUPDR_PUPDR0_0|GPIO_PUPDR_PUPDR3_0|GPIO_PUPDR_PUPDR4_0|GPIO_PUPDR_PUPDR5_0);//Pull up
35.	        
36.	    SET_BIT(GPIOC->MODER,GPIO_MODER_MODER1_0|GPIO_MODER_MODER2_0|GPIO_MODER_MODER6_0|GPIO_MODER_MODER7_0);//PC1,2,6,7 Out
37.	    SET_BIT(GPIOC->OTYPER, GPIO_OTYPER_OT_1|GPIO_OTYPER_OT_2|GPIO_OTYPER_OT_6|GPIO_OTYPER_OT_7); //режим с открытым стоком
38.	    SET_BIT(GPIOC->BRR,GPIO_BRR_BR_1|GPIO_BRR_BR_2|GPIO_BRR_BR_6|GPIO_BRR_BR_7); //притягиваем к нулю
39.	        
40.	    // Настраиваем приоритеты
41.	    NVIC_SetPriorityGrouping(4);
42.	    priGroup = NVIC_GetPriorityGrouping();
43.	    printf("Priority Group=%d\r\n",priGroup);
44.	        
45.	    NVIC_SetPriority(EXTI0_IRQn,11);
46.	    NVIC_DecodePriority(NVIC_GetPriority(EXTI0_IRQn),priGroup,&PreemptPriority,&SubPriority);
47.	    printf("EXTI0 Preempt Priority=%d \tSubPriority=%d\r\n",PreemptPriority,SubPriority);
48.	        
49.	    NVIC_SetPriority(EXTI3_IRQn,0);
50.	    NVIC_DecodePriority(NVIC_GetPriority(EXTI3_IRQn),priGroup,&PreemptPriority,&SubPriority);
51.	    printf("EXTI3 Preempt Priority=%d \tSubPriority=%d\r\n",PreemptPriority,SubPriority);
52.	    
53.	    NVIC_SetPriority(EXTI4_IRQn,1);
54.	    NVIC_DecodePriority(NVIC_GetPriority(EXTI4_IRQn),priGroup,&PreemptPriority,&SubPriority);
55.	    printf("EXTI4 Preempt Priority=%d \tSubPriority=%d\r\n",PreemptPriority,SubPriority);
56.	    
57.	    NVIC_SetPriority(EXTI9_5_IRQn,10);
58.	    NVIC_DecodePriority(NVIC_GetPriority(EXTI9_5_IRQn),priGroup,&PreemptPriority,&SubPriority);
59.	    printf("EXTI5 Preempt Priority=%d \tSubPriority=%d\r\n",PreemptPriority,SubPriority);
60.	    
61.	    printf("Press any key\r\n");
62.	    // Настраиваем прерывания
63.	        //прерывание на спад сигнала
64.	    SET_BIT(EXTI->FTSR,EXTI_FTSR_FT0|EXTI_FTSR_FT3|EXTI_FTSR_FT4|EXTI_FTSR_FT5);
65.	    //разрешаем прерывания внешних линий 2,3,4,6
66.	    SET_BIT(EXTI->IMR,EXTI_IMR_IM0|EXTI_IMR_IM3|EXTI_IMR_IM4|EXTI_IMR_IM5);
67.	    
68.	    //выбираем в качестве внешних входов EXTI порт C
69.	    SYSCFG->EXTICR[0]=SYSCFG_EXTICR1_EXTI3_PC|SYSCFG_EXTICR1_EXTI0_PC;
70.	    SYSCFG->EXTICR[1]=SYSCFG_EXTICR2_EXTI4_PC|SYSCFG_EXTICR2_EXTI5_PC;
71.	    
72.	    // Включаем обработчик прерываний
73.	    NVIC_EnableIRQ(EXTI0_IRQn);
74.	    NVIC_EnableIRQ(EXTI3_IRQn);
75.	    NVIC_EnableIRQ(EXTI4_IRQn);
76.	    NVIC_EnableIRQ(EXTI9_5_IRQn);
77.	    
78.	    SysTick_Config(0x6DDD00);//прерывание каждые 100мсек
79.	    
80.	    while(1){}
81.	}
82.	
83.	    
84.	void SysTick_Handler(void){ //обработчик прерывание системного тайме-ра
85.	    ui_cout100ms++;
86.	    if(ui_cout100ms%100==0)//выводим каждые 10 сек
87.	    printf("%d sec\n",ui_cout100ms/10);
88.	}
89.	    
90.	void EXTI0_IRQHandler(void){
91.	    EXTI->PR = EXTI_PR_PR0;
92.	    ITM_SendChar('0');
93.	    delay();
94.	    ITM_SendChar('a');
95.	    ITM_SendChar('\n');
96.	}
97.	    
98.	void EXTI3_IRQHandler(void){
99.	    EXTI->PR = EXTI_PR_PR3;
100.	    ITM_SendChar('3');
101.	    delay();
102.	    ITM_SendChar('b');
103.	    ITM_SendChar('\n');
104.	}
105.	    
106.	void EXTI4_IRQHandler(void) {
107.	    EXTI->PR = EXTI_PR_PR4;
108.	    ITM_SendChar('4');
109.	    delay();
110.	    ITM_SendChar('c');
111.	    ITM_SendChar('\n'); 
112.	}
113.	    
114.	void EXTI9_5_IRQHandler(void){
115.	    EXTI->PR = EXTI_PR_PR5;
116.	    ITM_SendChar('5');
117.	    delay();
118.	    ITM_SendChar('d');
119.	    ITM_SendChar('\n'); 
120.	}
