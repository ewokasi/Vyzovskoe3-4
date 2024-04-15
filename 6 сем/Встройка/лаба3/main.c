#include "RTE_Components.h"
#include CMSIS_device_header
void delay(volatile uint32_t count)
{
    while (count--)
        __NOP();
}
int main(void)
{
    // Вспомогательные переменные
    volatile uint32_t StartUpCounter = 0, HSEStatus = 0;
    SET_BIT(RCC->CR, RCC_CR_HSEON); // включаем HSE
    do
    { // ждем вхождения в работу HSE
        HSEStatus = RCC->CR & RCC_CR_HSERDY;
        StartUpCounter++;
    } while ((HSEStatus == 0) && (StartUpCounter != 0x5000));
    // если за 0x5000 итераций, HSE не запустился, то проблемы в аппаратуре
    if ((RCC->CR & RCC_CR_HSERDY) != RESET)
    {
        // настраиваем буфер FLASH предварительной выборки команд
        FLASH->ACR = FLASH_ACR_LATENCY_1;
        // настройка PLL на 24 МГц = 8 МГц(HSE)/4*12
        // сначала выключаем чтобы изменить биты PLL, после настройки включим
        CLEAR_BIT(RCC->CR, RCC_CR_PLLON);
        // PLLSRC=HSE/2
        // PLLCLK=PLLSRC * 10
        RCC->CFGR2 |= (uint32_t)RCC_CFGR2_PREDIV_DIV2;
        RCC->CFGR |= (uint32_t)(RCC_CFGR_PLLSRC_HSE_PREDIV | RCC_CFGR_PLLMUL100);
        SET_BIT(RCC->CR, RCC_CR_PLLON); // включаем PLL
        // ждём запуск и стабилизацию PLL
        while ((RCC->CR & RCC_CR_PLLRDY) == 0)
        {
        }
        // выбираем выход PLL источником тактирования МК
        RCC->CFGR |= (uint32_t)RCC_CFGR_SW_PLL;
        // Ожидаем установки PLL источником тактирования МК
        while ((RCC->CFGR & (uint32_t)RCC_CFGR_SWS) != (uint32_t)RCC_CFGR_SWS_PLL)
        {
        }
    }
    else
    {
        while (1)
        {
        }
    } // HSE не запустился
    // контролируем частоту тактирования 4/1=4 МГц
    SystemCoreClockUpdate(); // устанавливается в глобальной переменной SystemCoreClock
    // Настройка MCO на PLLCLK/2
    SET_BIT(RCC->CFGR, RCC_CFGR_MCO_PLL);

    SET_BIT(RCC->AHBENR, RCC_AHBENR_GPIOAEN); // разрешаем тактирование GPIOA
    // для PA8 устанавливаем Alternate function mode
    SET_BIT(GPIOA->MODER, GPIO_MODER_MODER8_1);
    // для восьмой линии выбираем AF0 режим работы MCO
    CLEAR_BIT(GPIOA->AFR[1], GPIO_AFRH_AFRH0_Msk);

    // разрешаем тактирование GPIOD
    SET_BIT(RCC->AHBENR, RCC_AHBENR_GPIODEN);
   

    // устанавливаем работу линий PD0,PA9 на вывод
    SET_BIT(GPIOD->MODER, GPIO_MODER_MODER0_0);
    SET_BIT(GPIOA->MODER, GPIO_MODER_MODER9_0);
    // линию PA9 в режим вывода с открытым стоком
    SET_BIT(GPIOA->OTYPER, GPIO_OTYPER_OT_9);
    // подтягиваем PA9 к питанию Pull-up
    SET_BIT(GPIOA->PUPDR, GPIO_PUPDR_PUPDR19_0);
    while (1)
    {
        // устанавливаем (1) на выходе линий PD0,PA9
        GPIOD->BSRR = GPIO_ODR_0;
        GPIOA->BSRR = GPIO_ODR_9;
        // delay(10); // задержка
        // сбрасываем в (0) выходы линий PD0,PA9
        GPIOD->BRR = GPIO_ODR_0;
        GPIOA->BRR = GPIO_ODR_9;
        // delay(10);
    }
}
