#include "RTE_Components.h" // Component selection
#include CMSIS_device_header // Device header
#define DELAY {__nop();__nop();__nop();__nop();} //задержка на 4ре такта

//void delay(volatile uint32_t count){//1 002 560 = 1sec
//while(count--)
//__nop();
//}

int main(void)
{
//Вспомогательные переменные, не модифицируемые компилятором 
volatile uint32_t StartUpCounter = 0, HSEStatus = 0;
// Clock control register (RCC_CR): Bit 16 HSEON:
// 0: HSE oscillator OFF; 1: HSE oscillator ON;
SET_BIT(RCC -> CR,RCC_CR_HSEON);// включаем HSE 
do {// ждем вхождения в работу HSE
HSEStatus = RCC->CR & RCC_CR_HSERDY;
StartUpCounter++;
} while((HSEStatus == 0) && (StartUpCounter != 0x5000));
//если за 0x5000 итераций, HSE не запустился, то проблемы в аппаратуре
if ((RCC->CR & RCC_CR_HSERDY) != RESET)
{ //HSE запустился
// настраиваем FLASH, время предварительной выборки в буфер команд 
//Flash access control register (FLASH_ACR): Bits 2:0 LATENCY[2:0]:
//000: Zero wait state, if 0 < HCLK ≤ 24 MHz
//001: One wait state, if 24 MHz < HCLK ≤ 48 MHz -> FLASH_ACR_LATENCY_0
//010: Two wait sates, if 48 < HCLK ≤ 72 MHz -> FLASH_ACR_LATENCY_1
//FLASH_ACR:Bit 4 PRFTBE: 
// 0: Prefetch is disabled
// 1: Prefetch is enabled -> FLASH_ACR_PRFTBE
FLASH->ACR = 0;
// Clock configuration register (RCC_CFGR): Bits 7:4 HPRE:
// 0xxx: SYSCLK not divided -> RCC_CFGR_HPRE_DIV1 
RCC->CFGR |= (uint32_t) RCC_CFGR_HPRE_DIV2;//AHB Pre = 2 согласно варианта
// настройка PLL на 28 МГц = 8 МГц(HSE)/4*14
// сначала выключаем чтобы изменить биты PLL, после настройки включим
CLEAR_BIT(RCC -> CR,RCC_CR_PLLON);
// RCC_CFGR : Bit 16 PLLSRC: 
// 0: HSI/2 selected as PLL input clock -> RCC_CFGR_PLLSRC_HSI_DIV2
// 1: HSE/PREDIV selected as PLL input clock -> RCC_CFGR_PLLSRC_HSE_PREDIV
// RCC_CFGR: Bits 21:18 PLLMUL: 
// 0000: PLL input clock x 14 -> RCC_CFGR_PLLMUL14 
RCC->CFGR |= (uint32_t)(RCC_CFGR_PLLSRC_HSE_PREDIV | RCC_CFGR_PLLMUL14);
// Clock configuration register 2 (RCC_CFGR2): Bits 3:0 PREDIV
// 0011: HSE input to PLL divided by 4 -> RCC_CFGR2_PREDIV_DIV4 
RCC->CFGR2 |= (uint32_t)RCC_CFGR2_PREDIV_DIV4;
// RCC_CR: включаем PLL Bit 24 PLLON: -> RCC_CR_PLLON
// 0: PLL OFF; 1: PLL ON 
SET_BIT(RCC -> CR,RCC_CR_PLLON);
// ждём запуск и стабилизацию PLL 
while((RCC->CR & RCC_CR_PLLRDY) == 0){}
// выбираем выход PLL источником тактирования МК
RCC->CFGR |= (uint32_t)RCC_CFGR_SW_PLL;
//Ожидаем установки PLL источником тактирования МК
while ((RCC->CFGR & (uint32_t)RCC_CFGR_SWS) != (uint32_t)RCC_CFGR_SWS_PLL){}
}
else
{ while(1){} } // HSE не запустился
//контролируем частоту тактирования 28/1=28 МГц
SystemCoreClockUpdate();//устанавливается в глобальной переменной SystemCoreClock
// RCC_CFGR: Настройка MCO на PLLCLK/2
// Bits 26:24 MCO:
// 100: System clock (SYSCLK) selected RCC_CFGR_MCO_SYSCLK 
// 111: PLL/2 clock selected RCC_CFGR_MCO_PLL 
SET_BIT(RCC -> CFGR, RCC_CFGR_MCO_PLL);
SET_BIT(RCC -> AHBENR,RCC_AHBENR_GPIOAEN); //разрешаем тактирование GPIOA
//для PA8 устанавливаем Alternate function mode
SET_BIT(GPIOA -> MODER,GPIO_MODER_MODER8_1);
//для восьмой линии выбираем AF0 режим работы MCO
CLEAR_BIT(GPIOA -> AFR[1], GPIO_AFRH_AFRH0_Msk);

//разрешаем тактирование GPIOC 
SET_BIT(RCC->AHBENR,RCC_AHBENR_GPIOCEN);
//разрешаем тактирование GPIOF 
SET_BIT(RCC->AHBENR,RCC_AHBENR_GPIOFEN);

//устанавливаем работу линий PC1,PF6 на вывод
SET_BIT(GPIOC->MODER,GPIO_MODER_MODER1_0);
SET_BIT(GPIOF->MODER,GPIO_MODER_MODER6_0);

//линию PF6 в режим однотактного вывода с открытым стоком
SET_BIT(GPIOF->OTYPER,GPIO_OTYPER_OT_6);

//подтягиваем PC1 к земле Pull-down, PF6 к питанию Pull-up
SET_BIT(GPIOC->PUPDR, GPIO_PUPDR_PUPDR1_1);
SET_BIT(GPIOF->PUPDR, GPIO_PUPDR_PUPDR6_1);

while(1){
//устанавливаем 1 на выходе линий PC1,PF6
GPIOC->BSRR= GPIO_ODR_1;
GPIOF->BSRR= GPIO_ODR_6;
DELAY DELAY;
// задержка на 8 тактов
    
//сбрасываем в 0 выходы линий PC1,PF6
GPIOC->BRR= GPIO_ODR_1;
GPIOF->BRR= GPIO_ODR_6;
DELAY DELAY;
 // задержка на 8 тактов
}
}
